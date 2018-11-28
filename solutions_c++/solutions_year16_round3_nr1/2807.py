#include<iostream>
#include<string>
#include<vector>

using namespace std;

string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

bool is_there(int senate[], int num)
{
    for(int k=0; k<num; k++)
    {
        if(senate[k] !=0)
        {
            return true;
        }
    }
    return false;
}

void findmax(int senate[], int num, vector<int> &max_index)
{
    int max=0;
    for(int l=0; l<num; l++)
    {
        if(max>=senate[l])
        {
            continue;
        }
        else
        {
            max = senate[l];
        }
    }
    if(max != 1)
    {
        for(int l=0; l<num; l++)
        {
            if(senate[l]==max)
            {         
                max_index.push_back(l);
            }
        }
    }
    else
    {
        max_index.push_back(-1);
        for(int l=0; l<num; l++)
        {
            if(senate[l]==max)
            {
                max_index.push_back(l);
            }
        }

    }

}


int main()
{
    int N;
    cin >> N;
    for(int i=0; i<N; i++)
    {
        int no_parties;
        cin >> no_parties;
        int senate[no_parties];
        for(int j=0; j<no_parties; j++)
        {
            cin>> senate[j];
        }
        cout<< "Case #" << i+1 <<":"<< " " ;
        while(is_there(senate, no_parties))
        {
            vector<int> max_index;
            findmax(senate, no_parties, max_index);
            if(max_index[0] >= 0)
            {
                if(max_index.size()==1)
                {
                    int temp;
                    temp = max_index[0];
                    int temp1 = senate[temp];
                    if(temp1 > 2)
                    {   
                        cout<< alphabet[temp] << alphabet[temp] << " ";
                        temp1 = temp1 - 2;
                        senate[temp] = temp1;
                    }
                    else
                    {   
                        cout << alphabet[temp] << " ";
                        temp1 = temp1 - 1;
                        senate[temp] = temp1;
                    }   
                }   
                else if(max_index.size() >= 2)
                {
                    int temp1;
                    int temp2;
                    temp1 = max_index[0];
                    temp2 = max_index[1];
                    cout << alphabet[temp1] << alphabet[temp2] << " ";
                    senate[temp1] -- ;
                    senate[temp2] -- ;
                }
            }
            else
            {
                if(max_index.size() == 3)
                {
                    int temp1;
                    int temp2;
                    temp1 = max_index[1];
                    temp2 = max_index[2];
                    cout << alphabet[temp1] << alphabet[temp2] << " ";
                    senate[temp1] -- ;
                    senate[temp2] -- ;
                }
                else
                {
                    int temp;
                    temp = max_index[1];
                    cout << alphabet[temp]<< " ";
                    senate[temp] -- ;
                }
            }            
        }
        cout << endl;
    }
    return 0;
}



