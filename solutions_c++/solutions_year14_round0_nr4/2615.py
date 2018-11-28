#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;
int compare(const void*a,const void*b){
    return (*(int*)a-*(int*)b);
}

int main()
{
    int t,l=1;
    ifstream cin("D-small-attempt0.in");
	ofstream cout("e.txt");
    cin>>t;
    while(t--){
        int n,war=0,dwar=0,j,i;
        float naomi[1000],ken[1000];
        cin>>n;
        for(i=0;i<n;i++){
            cin>>naomi[i];
        }
        qsort(naomi,n,sizeof(float),compare);
        for(i=0;i<n;i++){
            cin>>ken[i];
        }
        qsort(ken,n,sizeof(float),compare);
        cout<<"Case #"<<l<<": ";
        //dwar
        j=0;
        for(i=0;i<n;i++){
            if(ken[i]>naomi[j]){

                    j++;
                    if(j>=n)
                        break;
                    i--;

            }


            else{
                dwar++;
                j++;
                if(j>=n)
                    break;
            }
        }


        cout<<dwar<<" ";

        //war
        j=n-1;

        for(i=n-1;i>=0;i--){
            if(naomi[i]>ken[j]){
                war++;

            }
            else{
                j--;
            }

        }
        cout<<war<<endl;
        l++;

    }



}
