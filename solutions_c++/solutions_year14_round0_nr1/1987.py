#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,x,y,c,first,second;
    int arr1[4][4],arr2[4][4];
    cin>>T;
    for(int i=1;i<=T;++i){
        cin>>first;
        for(int j=0;j<4;++j){
            for(int k=0;k<4;++k){
                cin>>arr1[j][k];
            }
        }
        cin>>second;
        for(int j=0;j<4;++j){
            for(int k=0;k<4;++k){
                cin>>arr2[j][k];
            }
        }

        sort(arr1[first-1],arr1[first-1]+4);
        sort(arr2[second-1],arr2[second-1]+4);

        int cnt=0,p1=0,p2=0,num=-1;
        while(p1<4&&p2<4){
            if(arr1[first-1][p1]==arr2[second-1][p2]){

                num=arr1[first-1][p1];
                ++cnt,++p1,++p2;
            }
            else if(arr1[first-1][p1] > arr2[second-1][p2]){
                ++p2;
            }else {
                ++p1;
            }
        }
        cout<<"Case #"<<i<<": ";
        switch(cnt){
        case 0:
                printf("Volunteer cheated!\n");
                break;
        case 1:
                cout<<num<<endl;
                break;
        default:
                printf("Bad magician!\n");

        }
    }

    return 0;
}
