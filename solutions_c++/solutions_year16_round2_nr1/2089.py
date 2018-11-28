#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

string num[10]= {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int shu[10]={0,2,8,6,7,3,4,5,1,9};
string item;
int mark[128];
string ans;
void call()
{
    int k;
    for(int i=0; i<item.length(); ++i)
    {
        mark[item[i]]++;
    }

    for(int j=0; j<10; j++)
    {
        while(1)
        {


            for( k=0; k < num[shu[j]].length() ; k++)
            {
                if(mark[num[shu[j]][k]]==0)
                {
                    break;
                }
            }

            if(k!=num[shu[j]].length())
                break;
            else
            {


                for( k=0; k < num[shu[j]].length() ; k++)
                {
                    mark[num[shu[j]][k]]--;
                }
                ans=ans+char(shu[j]+'0');
            }
        }
    }


    std::stable_sort(&(ans[0]),&(ans[0])+ans.length());
   cout<<ans<<endl;
}
int main()
{
    int n;
    cin>>n;

    for(int i=0; i<n; i++)
    {
        cin>>item;
        cout<<"Case #"<<i+1<<": ";
        memset(mark,0,sizeof(mark));
        ans="";
        call();
    }


    return 0;
}
