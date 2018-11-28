#include <bits/stdc++.h>
#define LL long long int
#define mod 1000000007
using namespace std;
int t,t1=1;




int main(){
    std::ios_base::sync_with_stdio(false);
ofstream outputFile("out.txt");
    cin>>t;
    while(t--){
        string s;
         int c[1000]={0};
        int a[2000]={0};
        int k=0;
        cin>>s;
        for(int i=0;i<s.length();i++){
            c[(int)s[i]]++;

        }
        //zero z
        if(c[(int)'Z']>0){

            while(c[(int)'Z']--){
                a[k]=0;
                k++;
                c[(int)'E']--;
                c[(int)'R']--;
                c[(int)'O']--;
            }


        }
        //Two= w
        if(c[(int)'W']>0){

            while(c[(int)'W']--){
                a[k]=2;
                k++;
                c[(int)'T']--;
                c[(int)'O']--;
            }


        }
                //Four U
        if(c[(int)'U']>0){

            while(c[(int)'U']--){
                a[k]=4;
                k++;
                c[(int)'F']--;
                c[(int)'O']--;
                c[(int)'R']--;
            }


        }
        if(c[(int)'X']>0){

            while(c[(int)'X']--){
                a[k]=6;
                k++;
                c[(int)'S']--;
                c[(int)'I']--;

            }


        }
        //Eight G
        if(c[(int)'G']>0){

            while(c[(int)'G']--){
                a[k]=8;
                k++;
                c[(int)'E']--;
                c[(int)'I']--;
                c[(int)'H']--;
                c[(int)'T']--;
            }


        }



        //Three

        if(c[(int)'R']>0){

            while(c[(int)'R']--){
                a[k]=3;
                k++;
                c[(int)'E']--;
                c[(int)'E']--;
                c[(int)'T']--;
                c[(int)'H']--;
            }


        }


        //Six x

        //Five     f
        if(c[(int)'F']>0){

            while(c[(int)'F']--){
                a[k]=5;
                k++;
                c[(int)'I']--;
                c[(int)'V']--;
                c[(int)'E']--;
            }


        }
        //seven V
        if(c[(int)'V']>0){

            while(c[(int)'V']--){
                a[k]=7;
                k++;
                c[(int)'S']--;
                c[(int)'E']--;
                c[(int)'E']--;
                c[(int)'N']--;
            }


        }
        //one o
        if(c[(int)'O']>0){

            while(c[(int)'O']--){
                a[k]=1;
                k++;
                c[(int)'E']--;
                c[(int)'N']--;
            }


        }
        if(c[(int)'I']>0){

            while(c[(int)'I']--){
                a[k]=9;
                k++;
                c[(int)'N']--;
                c[(int)'E']--;
                c[(int)'N']--;
            }


        }




    sort(a,a+k);
    cout<<"Case #"<<t1<<": ";
    outputFile<<"Case #"<<t1<<": ";
    for(int i=0;i<k;i++){
        cout<<a[i];
        outputFile<<a[i];
    }
    cout<<endl;
    outputFile<<endl;
    t1++;

    }


return 0;
}
