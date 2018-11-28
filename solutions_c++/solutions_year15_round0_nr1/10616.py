#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t_case;
    cin>>t_case;
    for(int i=0;i<t_case;i++)
    {
    int shy_level,person_stand=0,person_needed=0;
    cin>>shy_level;
    int shy_index[shy_level+1];
    string s;
    cin>>s;
    for(int j=0;j<s.size();j++)
    {
        int inp;
        inp=s[j]-'0';
        shy_index[j]=inp;
    }
    for(int j=0;j<=shy_level;j++)
    {
        if(shy_index[j]==0)
        {
          continue;
        }
        else{
        if(j>person_stand)
        {
            person_needed+=j-person_stand;
            person_stand+=(j-person_stand)+shy_index[j];
        }
       else if(j<=person_stand)
        person_stand+=shy_index[j];
        }
    }
    cout<<"Case #"<<i+1<<": "<<person_needed<<"\n";
    }
    return 0;
}
