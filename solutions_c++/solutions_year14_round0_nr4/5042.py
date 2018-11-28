#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
int tcase;
cin>>tcase;
for(int i=0;i<tcase;i++){
    int num;
    cin>>num;
    double a[num];
    double b[num];
    for(int k=0;k<num;k++)
        cin>>a[k];

    for(int k=0;k<num;k++)
        cin>>b[k];

    sort(a,a+num);
    sort(b,b+num);
/*
    for(int k=0;k<num;k++)
        cout<<a[k]<<" ";
         cout<<endl;

    for(int k=0;k<num;k++)
        cout<<b[k]<<" ";
        cout<<endl;
*/
    int k=0;
    int j=0;
    while(k!=num){
    if(a[j]<b[k])
    j++;
    k++;
    }


    int remain=num-j;

   vector <double> girl;
        vector <double> boy;

     for ( int k = 0; k < num; k++ ){
            girl.push_back(a[k]);
             boy.push_back(b[k]);
        }


        int score = 0;


        for ( int k = 0; k < num; ++k ){
            if ( girl[k] <  boy[0] ){
                 boy.erase( boy.begin() +  boy.size() - 1);
            }
            else {
                ++score;
                 boy.erase(boy.begin());
            }
        }

    cout<<"Case #"<<i+1<<":"<<" "<<score<<" "<<remain<<endl;

}
}
