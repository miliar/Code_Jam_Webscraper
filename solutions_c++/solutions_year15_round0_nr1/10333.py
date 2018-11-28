#include<iostream>

using namespace std;

void inputs();
void process();
int smax,nfriends=0,t,l=0,naud=0,x=0;
char sx[1008];
int s[1008];

int main()
{
    
    cin >> t;
    for(int i=0;i <t; i++)
    {
    
        cin >> smax;
        l=smax+1;
        inputs();
        process();
        
        cout << "Case #" << i+1 << ":" << " " << nfriends << endl ;

        nfriends=0;
        naud=0;
        x=0;
        smax=0;
        
    }
    
    
    return 0;
}

void inputs()
{
    for (int i=0;i < l; i++ )
    {
        cin >> sx[i];
        s[i]=sx[i]%48;
    }
}
void process()
{
    int i;
    
    naud=s[0];
    
    for( i=1;i <l ; i++)
    {
        if (s[i]==0)
            continue;
        if ( i > naud)
        {
            x= i - naud ;
            naud = naud + x + s[i]  ;
            nfriends= nfriends +x;
        }
        else
            naud=naud+ s[i];
        
    }
    
}

