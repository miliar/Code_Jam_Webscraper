#include<bits/stdc++.h>
using namespace std;
int main()
{
    int casos,caso=1;
    cin>>casos;
    string s;
    while(casos--)
    {
        cin>>s;
        string res;
        string aux;
        res.push_back(s[0]);
        for(int i=1;i<s.size();i++)
        {
            if(s[i]>=res[0])
                {
                    aux="";
                    aux.push_back(s[i]);
                    res=aux+res;
                }
            else
                res.push_back(s[i]);
        }
        printf("Case #%d: ",caso++);
        cout<<res<<endl;
    }
    return 0;
}
