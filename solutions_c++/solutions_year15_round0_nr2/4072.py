#include <iostream>

using namespace std;

int A[10];
int B[10];

int main()
{
    int z;
    cin>>z;
    for(int t=1; t<=z; t++)
    {
        int n;
        cin>>n;

        for(int i=1; i<=9; i++) A[i]=0;
                for(int i=1; i<=9; i++) B[i]=0;

        for(int i=1; i<=n; i++)
        {
            int x;
            cin>>x;
            A[x]++;
            B[x]++;

        }

        int maxczas;
        for(int i=9; i>=1; i--)
        {
            if(A[i]!=0)
            {
                maxczas=i;
                break;
            }
        }

        bool koniec=false;
        int czasmin=maxczas;
        int zmiany=0;
        for(int l=maxczas; l>=4; l--)
        {
            if(l==9 && koniec==false)
            {
                if(A[9]<=3)
                {
                    zmiany+=A[9];
                    A[5]+=A[9];
                    A[4]+=A[9];
                    A[9]=0;

                    for(int i=8; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            if(l==8 && koniec==false)
            {
                if(A[8]<=3)
                {
                    zmiany+=A[8];
                    A[4]+=2*A[8];
                    A[8]=0;

                    for(int i=7; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            if(l==7 && koniec==false)
            {
                if(A[7]<=2)
                {
                    zmiany+=A[7];
                    A[4]+=A[7];
                    A[3]+=A[7];
                    A[7]=0;

                    for(int i=6; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}


             }

            if(l==6 && koniec==false)
            {
                if(A[6]<=2)
                {
                    zmiany+=A[6];
                    A[3]+=2*A[6];
                    A[6]=0;

                    for(int i=5; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{koniec=true;}
             }

            if(l==5 && koniec==false)
            {
                if(A[5]<=1)
                {
                    zmiany+=A[5];
                    A[3]+=A[5];
                    A[2]+=A[5];
                    A[5]=0;

                    for(int i=4; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{koniec=true;}
             }

            if(l==4 && koniec==false)
            {
                if(A[4]<=1)
                {
                    zmiany+=A[4];
                    A[2]+=2*A[4];
                    A[4]=0;

                    for(int i=3; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            }

            zmiany=0;
            koniec=false;
            for(int i=1; i<=9; i++) A[i]=B[i];

        for(int l=maxczas; l>=4; l--)
        {
            if(l==9 && koniec==false)
            {
                if(A[9]<=3)
                {
                    zmiany+=2*A[9];
                    A[3]+=3*A[9];
                    A[9]=0;

                    for(int i=8; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            if(l==8 && koniec==false)
            {
                if(A[8]<=3)
                {
                    zmiany+=A[8];
                    A[4]+=2*A[8];
                    A[8]=0;

                    for(int i=7; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            if(l==7 && koniec==false)
            {
                if(A[7]<=2)
                {
                    zmiany+=A[7];
                    A[4]+=A[7];
                    A[3]+=A[7];
                    A[7]=0;

                    for(int i=6; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}


             }

            if(l==6 && koniec==false)
            {
                if(A[6]<=2)
                {
                    zmiany+=A[6];
                    A[3]+=2*A[6];
                    A[6]=0;

                    for(int i=5; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{koniec=true;}
             }

            if(l==5 && koniec==false)
            {
                if(A[5]<=1)
                {
                    zmiany+=A[5];
                    A[3]+=A[5];
                    A[2]+=A[5];
                    A[5]=0;

                    for(int i=4; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{koniec=true;}
             }

            if(l==4 && koniec==false)
            {
                if(A[4]<=1)
                {
                    zmiany+=A[4];
                    A[2]+=2*A[4];
                    A[4]=0;

                    for(int i=3; i>=1; i--)
                    {
                        if(A[i]!=0)
                        {
                            if(czasmin>zmiany+i) czasmin=zmiany+i;
                            break;
                        }
                    }
                 }
                 else{
                 koniec=true;}
             }

            }


             cout<<"Case #"<<t<<": "<<czasmin<<endl;

        }



    return 0;
}
