#include<bits/stdc++.h>
using namespace std;
bool contar(string num,bool reps[])
{
    for(int i=0; i<num.size(); i++)
        reps[num[i]-'0']=true;
    for(int i=0; i<10; i++)
        if(!reps[i])
            return false;
    return true;
}

int main()
{
    int casos=0,caso=1;
    long long int n=0;
    cin>>casos;
    while(casos--)
    {
        bool reps[10]= {0};
        long long int resp=0;
        long long int it=1;
        cin>>n;
        if(n!=0)
        {
            while(true)
            {
                resp=n*it;
                stringstream ss;
                ss<<resp;
                if(contar(ss.str(),reps)==true)
                    break;
                it++;

            }
            printf("Case #%d: %lld\n",caso++,resp);
        }
        else
            printf("Case #%d: INSOMNIA\n",caso++);

    }
    return 0;
}
