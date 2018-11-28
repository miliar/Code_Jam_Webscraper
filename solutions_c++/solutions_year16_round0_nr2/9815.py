#include <iostream>
using namespace std ;
int main ()
{
    int T ;
    int v=0;
    string N;
    int w;
    cin>>T ;
    int y=T ;
    int p=0 ;
    int q=0 ;
    int arr[y];
    while (T--)
    {
        cin>>N ;
        for (int i=0 ; i<N.size()-1 ; i++)
        {
            if (N[i]!=N[i+1])
                v++;

        }
        if (N[N.size()-1] == '-')
            v++ ;
        arr[q]=v ;
        q++ ;
        v=0;
    }
    for (int l=0 ; l<y ; l++ )
    {
        p++;
        cout<<"Case #"<<p<<": "<< arr[l]<<"\n" ;

    }
cin>>w;
}
