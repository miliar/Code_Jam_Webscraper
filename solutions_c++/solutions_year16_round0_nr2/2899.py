#include<bits/stdc++.h>


using namespace std;

#define f(i,a, b) for(int i=a; i<=b; i++)

int main()
{
    int T;

    cin>>T;
    char c,aux, ant='\0';
    int resp =0;

   scanf("%c", &c);

    f(t, 1, T)
    {
        resp = 0; ant=aux=c='\0';

        for(; ; )
        {
            scanf("%c", &aux);
            //cout<<"aux "<<aux<<endl;

            if(aux=='\n')
                break;

            c=aux;

            if(ant!='\0' && c!=ant)
            {
                resp++;

            }
            ant = c;

        }

        if(c == '-')
            resp++;

        cout<<"Case #"<<t<<": "<<resp<<endl;
    }



    return 0;
}
