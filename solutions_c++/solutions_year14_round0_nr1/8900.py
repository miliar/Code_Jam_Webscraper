#include <iostream>
#include<fstream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen ("A-small-attempt1.in","r",stdin);
    freopen ("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        short int arr[4][4];
        short int arr2[4][4];
        short int p1,p2;
        short int diff=-1,mag=0;
        cin>>p1;
        p1--;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                cin>>arr[j][k];

            }
        }

        cin>>p2;
        p2--;
        for(int j=0; j<4; j++)
        {
            for(int k=0; k<4; k++)
            {
                cin>>arr2[j][k];

            }
        }

        for(int j=0; j<4; j++){
           for(int k=0; k<4; k++){
        if(arr[p1][k ]== arr2[p2][j])
        {
            diff++;
            mag = arr2[p2][j];

        }
        }}
        if(diff == 0){
        cout<<"Case #"<<i+1<<": "<<mag<<endl;
        }
        else if(diff > 0){
        cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
        }
        else
        cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }


    return 0;
}
