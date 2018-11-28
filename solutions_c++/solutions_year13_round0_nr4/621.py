#include <string>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int keys_count;
int chest_opened;

int key_number;
int chest_number;

vector<int> moves;

int keys[201] = {0};

bool path_to_type[201] = {false};

int keys_all[201] = {0};
int chests_all[201] = {0};

int chest_types[201] = {0};
bool opened[201] = {false};

vector<int> keys_in_chests[201];
vector<int> type_chest[201];

bool Check()
{
    for(int i = 1; i < 201; ++i)
    {
        if(keys_all[i] < chests_all[i])
        {
            return false;
        }
    }
    return true;
}

bool CheckPath()
{
    vector<int> nn;
    vector<int> kk;

    for(int i = 1; i <= chest_number; ++i)
    {
        if(!opened[i]) nn.push_back(chest_types[i]);
    }

    for(int i : nn)
    {
        path_to_type[i] = false;
    }

    for(int i = 0; i < 201; ++i)
    {
        if(keys[i])
        {
            kk.push_back(i);
        }
    }

    while(!kk.empty())
    {
        int i = kk.back();
        kk.pop_back();

        path_to_type[i] = true;
        for(int j : type_chest[i])
        {
            for(int m : keys_in_chests[j])
            {
                if(!path_to_type[m])
                {
                    kk.push_back(m);
                }
            }
        }
    }

    for(int i : nn)
    {
        if(!path_to_type[i]) return false;
    }
    return true;
}

void GetKey(int key)
{
    --keys[key];
    --keys_count;
}

void ReturnKey(int key)
{
    ++keys_count;
    ++keys[key];
}

int FindNextChest(int prev_chest, int &key_type)
{
    for(int i = prev_chest + 1; i <= chest_number; ++i)
    {
        if(!opened[i] && keys[chest_types[i]]>0)
        {
            key_type = chest_types[i];
            return i;
        }
    }
    return 0;
}

void OpenChest(int chest)
{
    moves.push_back(chest);
    --chests_all[chest_types[chest]];
    opened[chest] = true;
    ++chest_opened;
    for(int i : keys_in_chests[chest])
    {
        ++keys[i];
        ++keys_count;
    }
}

void CloseLastChest()
{
    int last_chest = moves.back();
    moves.pop_back();
    opened[last_chest] = false;
    --chests_all[chest_types[last_chest]];
    --chest_opened;
    for(int i : keys_in_chests[last_chest])
    {
        --keys[i];
        --keys_count;
    }
}

bool CheckChests()
{
    for(int i = 1; i <= chest_number; ++i )
    {
        if(!opened[i]) return false;
    }
    return true;
}

bool ProcessStep()
{
    int current_key = 0;
    int current_chest = 0;
    while((current_chest = FindNextChest(current_chest, current_key)))
    {
        GetKey(current_key);
        OpenChest(current_chest);
        if(CheckPath())
        {
            if(chest_opened == chest_number) return true;
            if(keys_count)
            {
                if( ProcessStep() ) return true;
            }
        }
        CloseLastChest();
        ReturnKey(current_key);
    }
    return false;
}

int main()
{
    int case_number;
    cin >> case_number;

    for(int current = 1; current <= case_number; ++current)
    {
        cin >> key_number;
        cin >> chest_number;

        for(int i = 0; i < 201; ++i)
        {
            keys[i] = 0;
            keys_all[i] = 0;
            chests_all[i] = 0;
            chest_types[i] = 0;
            opened[i] = false;
            type_chest[i].clear();
        }

        for(int i = 0; i < key_number; ++i)
        {
            int c;
            cin >> c;
            ++keys[c];
            ++keys_all[c];
        }

        for(int i = 1; i <= chest_number; ++i)
        {
            cin >> chest_types[i];
            ++chests_all[chest_types[i]];
            type_chest[chest_types[i]].push_back(i);
            int c;
            cin >> c;
            keys_in_chests[i].clear();
            while(c--)
            {
                int k;
                cin >> k;
                keys_in_chests[i].push_back(k);
                ++keys_all[k];
            }
        }



        if(!Check() || !key_number)
        {
            cout << "Case #" << current << ": IMPOSSIBLE" << endl;
            continue;
        }

        keys_count = key_number;
        chest_opened = 0;

        moves.clear();

        if(ProcessStep())
        {
            cout << "Case #" << current << ": ";
            for(int i : moves)
            {
                cout << i << " ";
            }
        }
        else
        {
            cout << "Case #" << current << ": IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
