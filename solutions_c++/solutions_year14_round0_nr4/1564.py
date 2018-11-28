#include <iostream>
#include <algorithm>
using namespace std;

int compare (const void * a, const void * b)
{
  if ( *(double*)a <  *(double*)b ) return -1;
  if ( *(double*)a == *(double*)b ) return 0;
  if ( *(double*)a >  *(double*)b ) return 1;
}
int main(){
    int t, n, inh, inl, ikh, ikl, ch, cl;
    
    cin>>t;
    for(int k=1; k<=t; k++){
        cin>>n;
        inh = ch= 0;
        ikl = cl = 0;

        double nao[n];
        double ken[n];
        for(int i=0;i<n;i++){
            cin>>nao[i];
        }
        for(int i=0;i<n;i++){
            cin>>ken[i];
        }
        qsort (nao, n, sizeof(double), compare);
        qsort (ken, n, sizeof(double), compare);
        /*for(int i=0;i<n;i++){
            cout<<nao[i]<<" ";
        }
        cout<<"\n";
        for(int i=0;i<n;i++){
            cout<<ken[i]<<" ";
        }
        cout<<"\n";
        */
        for(int i=0;i<n;i++){
            if(ken[i]>nao[inh]){
                ch++;
                inh++;
            }
            if(inh>=n)
                break;
        }
        for(int i=0;i<n;i++){

            if(nao[i]>ken[ikl]){
                cl++;
                ikl++;
            }

            if(ikl>=n)
                break;
        
        }
        
        cout<<"Case #"<<k <<": "<< cl <<" "<< n-ch<<"\n";
    }
    return 0;
}
