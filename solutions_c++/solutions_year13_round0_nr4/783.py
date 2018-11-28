#include <set>
#include <list>
#include <vector>
#include <map>
#include <iostream>


using namespace std;

struct Chest
{
        map<int,int> _keys;
        int _key_type;
        int _n;
        bool _closed;
        Chest():_closed(true){}
};


bool testChest(map<int,int> &ourKeys,
               list<Chest*> &currentClosed,
               vector<Chest*> &currentOpen,
               set<Chest *> &currentOpenSet,
               int openCount,
               set<set<Chest *> > &alreadyTestedSet)
{
    if(openCount == 0)
    {
        return true;
    }
    
    
    if (alreadyTestedSet.insert(currentOpenSet).second == false)
    {
        return false;
    }

    for (auto itClosed = currentClosed.begin();itClosed != currentClosed.end();++itClosed)
    {
        Chest &c = **itClosed;
        if(!c._closed)
        {
            continue;
        }

        auto &keyCount = ourKeys[c._key_type];
        if(keyCount > 0)
        {
            --keyCount;
            //auto itForInsert = currentClosed.erase(itClosed);
            c._closed = false;
            currentOpen.push_back(&c);
            auto itInSet = currentOpenSet.insert(&c);
            for(auto itKeyInChest = c._keys.begin();itKeyInChest!= c._keys.end();++itKeyInChest)
            {
                ourKeys[itKeyInChest -> first] += itKeyInChest -> second;
            }

            if (testChest(ourKeys,
                          currentClosed,
                          currentOpen,
                          currentOpenSet,
                          openCount - 1,
                          alreadyTestedSet))
            {
                return true;
            }

            for(auto itKeyInChest = c._keys.begin();itKeyInChest!= c._keys.end();++itKeyInChest)
            {
                ourKeys[itKeyInChest -> first] -= itKeyInChest -> second;
            }
            currentOpen.pop_back();
            currentOpenSet.erase(itInSet.first);
            //itClosed = currentClosed.insert(itForInsert,&c);
            c._closed=true;
            ++keyCount;
        }
    }
    return false;
}

int main()
{
    unsigned int pb_total;
    cin >> pb_total;
   
    for (unsigned int pb_idx = 1;pb_idx <= pb_total;++pb_idx)
    {
        cerr << "Case #" << pb_idx << endl;

        int K, N;
        cin >> K >> N;

        map<int,int> ourKeys;
        for(int k = 1; k <= K;++k)
        {
            int key;
            cin >> key;
            ourKeys[key]+=1;
        }


        list<Chest> chests;
        
        for (int n = 1;n <= N;++n)
        {
            int Ti,Ki;
            cin >> Ti >> Ki;
            chests.push_back(Chest());
            Chest& chest= chests.back();
            chest._n = n;
            chest._key_type = Ti;
            for (int k=1; k <= Ki;++k)
            {
                int aKey;
                cin >> aKey;
                chest._keys[aKey]+=1;
            }
        }

        list<Chest *> closedChests;
        for (auto &c:chests)
        {
            closedChests.push_back(&c);
        }

        vector<Chest *> currentOpen;
        set<Chest *> currentOpenSet;
        set <set <Chest *> > alreadyTestedSet;
        
        bool r = testChest(ourKeys,
                           closedChests,
                           currentOpen,
                           currentOpenSet,
                           N,
                           alreadyTestedSet);
        
        cout << "Case #" << pb_idx << ":"; 
        
        if (r)
        {
            for (auto & c:currentOpen)
            {
                cout << " " << c->_n;
            }
            cout << endl;
        }
        else
        {
            cout << " IMPOSSIBLE" << endl;
        }
    }

}


