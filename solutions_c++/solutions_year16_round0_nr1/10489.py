#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<long long int> checklist;

void CheckIfFallsAsleep(long long int num , int count)
{
    int i = 1;

    long long int temp = 0;

    if(num==0)
        cout<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
    else
    {
        int counter = 1;
        while(checklist.size())
        {
            temp = 0;
            temp = counter * num;
            string str = to_string(temp);

            for(int i = 0 ; i < str.length() ; i++)
            {
				int digit = str[i] - '0';
                //cout<<"Looking for "<<digit<<endl;
                auto it = find (checklist.begin(), checklist.end(), digit);
                if (it != checklist.end())
                {
                   // cout<<"Erasing "<<*it<<endl;
                    checklist.erase(it);
                }
            }

            counter++;
        }
        
        cout<<"Case #"<<count<<": "<<temp<<endl;
    }


}

void FillCheckList()
{
	
	checklist.clear();
	for(int i = 0 ; i <10 ; i++)
    {
        checklist.push_back(i);
    }
}

int main()
{
    int testcases;
    int count = 0;


    cin>>testcases;
    while(testcases--)
    {
		FillCheckList();
        long long int num;
        cin>>num;
        ++count;
        CheckIfFallsAsleep(num , count);
    }

    return 0;
}
