#include<iostream>
#include<cstdio>
#include<fstream>
#include<set>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int t;
    int a;
    int arr[4][4];
    int b;
    vector<int> :: iterator it1;
    //set<int> :: iterator it2;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int brr[4][4];
    scanf("%d",&t);
    for(int z=0;z<t;z++){
        vector<int> v(8);
        vector<int> sa;
        vector<int> sb;
        scanf("%d",&a);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&arr[i][j]);
                if(i+1==a){
                    sa.push_back(arr[i][j]);
                }
            }
        }
        sort(sa.begin(),sa.begin()+4);
        scanf("%d",&b);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&brr[i][j]);
                if(i+1==b){
                    sb.push_back(brr[i][j]);
                }
            }
        }
        sort(sb.begin(),sb.begin()+4);
        it1=set_intersection (sa.begin(), sa.begin()+4, sb.begin(), sb.begin()+4, v.begin());
         v.resize(it1-v.begin());
         /*for(it1=v.begin();it1!=v.end();++it1){
            cout<<"enter"<<*it1<<"   ";
         }
         cout<<endl;*/
         if(v.size()==1){
            printf("Case #%d: %d\n",z+1,v[0]);
         }
         else if(v.size()>1){
            printf("Case #%d: Bad magician!\n",z+1);
         }
         else{
            printf("Case #%d: Volunteer cheated!\n",z+1);
         }
    }
    return 0;
}
