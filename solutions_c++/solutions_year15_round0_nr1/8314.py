#include<bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("output_qualification_A.txt","w",stdout);
    int t,m,invite,temp,stand,len;
    string s;
    vector<int> shyness;

    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
        invite=0;stand=0;s.clear();shyness.clear();
        cin>>m>>s;
        for(int i=0;i<s.size();i++)
            shyness.push_back(s[i]-'0');
        len=shyness.size();
        for(int i=0;i<len;i++)
        {
            temp=0;
            if(i>stand){
            temp+=i-stand;
            stand+=temp;
            }
            invite+=temp;
            stand+=shyness[i];
        //printf("step #%d: %d\n",i,invite);
        }
        printf("Case #%d: %d\n",cas,invite);
    }

    return 0;
}
