#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    for (int i = 1 ;i <= n ; i++)
    {
        string s;
        cin>>s;
        int cont=0;
        for (int j = s.size()-1 ; j >= 0 ; j--)
        {
            if (s[j]=='-')
            {
                if (s[0]=='+')
                {
                    for (int k = 0 ; k <= j ; k++)
                    {
                        if (s[k]=='-')
                        {
                            cont++;
                            break;
                        }
                        else
                        {
                            s[k]='-';
                        }
                    }
                }
                reverse(s.begin(),s.begin()+j+1);
                for(int k = 0 ; k <= j ; k++)
                    if (s[k]=='-')
                        s[k]='+';
                    else
                        s[k]='-';
                cont++;

            }

        }
        cout<<"Case #"<<i<<": "<<cont<<endl;
    }
    return 0;
}
