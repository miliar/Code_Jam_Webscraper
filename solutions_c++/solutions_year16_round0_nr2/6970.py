#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n , t ,j , k , cnt = 0;
    string s;
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cnt =0;
        cin>>s;
        j = s.size();
        while(j >=0)
        {
            if(s[j] == '-')
            {
                cnt++;
                k = j;
                while(k>=0)
                {
                    if(s[k] == '+')
                    {
                        s[k] = '-';
                    }
                    else
                    {
                        s[k] = '+';
                    }
                    k--;
                }
            }
            j--;
        }
        cout<<"Case #"<<i+1<<":"<<" "<<cnt<<endl;
    }


    return 0;
}
