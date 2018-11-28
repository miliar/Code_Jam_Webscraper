#include <cstdlib>
#include <iostream>
#include <bits/stdc++.h>



using namespace std;
#define decimal double

decimal buscarMarcar(vector<decimal> &v,vector<bool> &m,decimal &a,bool retornar){
    decimal j=-1;
    bool sw=true;
    for (int i=0;i<v.size();i++){
        if(m[i]==false){
            if(sw){
                j=i;
            }
            sw=false;
            if((v[i]-a)>=0){
                m[i]=true;
                if (retornar){
                    return 1;
                }else{
                    return 0;
                }

            }
        }
    }
    m[j]=true;
    if (retornar){
        return 0;
    }else{
        return 1;
    }


}

decimal function_(vector<decimal> &v1,vector<decimal> &v2,bool retornar){
    vector<bool> marcas(v1.size(),false);
    decimal acum=0;
    for (int i=0;i<v1.size();i++){
        acum+=buscarMarcar(v1,marcas,v2[i],retornar);
    }
    return acum;

}



int main(int argc, char *argv[])
{
   ifstream cin("D-large.in");
//    ifstream cin("entrada.txt");
ofstream cout("D-large.txt");

    long long int case_=0;
    decimal c=0,f=0,x;
    decimal acumTime,cps,r;
    cin>>case_;
    for (int k=1;k<=case_;k++){
            cin>>c;
            vector<decimal> vN;
            vector<decimal> vK;

            for (int i=0;i<c;i++){
               cin>>f;
               vN.push_back(f);
            }
            for (int i=0;i<c;i++){
               cin>>f;
               vK.push_back(f);
            }
            sort(vN.begin(),vN.end());
            sort(vK.begin(),vK.end());


              cout<<"Case #"<<k<<": "<<function_(vN,vK,true)<<" "<<function_(vK,vN,false)<<endl;


    }


    return 0;
}

