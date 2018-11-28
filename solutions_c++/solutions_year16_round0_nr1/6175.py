#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    for (int i = 1 ; i <= n ; i++)
    {
        int a;
        cin>>a;
        if (a==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
            int cont=1;
            vector <bool> vec(10,false);
            long long int resp;
            while (true)
            {
                char arr[20];
                itoa(cont*a,arr,10);
                resp=cont*a;
                for (int j = 0 ; j < strlen(arr) ; j++)
                {
                    vec[arr[j]-48]=true;
                }
                bool fin=true;
                for (int j = 0 ; j < 10 ; j++)
                {
                    if (!vec[j])
                    {
                        fin=false;
                        break;
                    }
                }
                if(fin)
                {
                    cout<<"Case #"<<i<<": "<<resp<<endl;
                    break;
                }
                cont++;
            }
        }
    }
    return 0;
}
