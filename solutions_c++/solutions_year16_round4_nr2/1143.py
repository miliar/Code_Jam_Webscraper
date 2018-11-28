#include<bits/stdc++.h>
using namespace std;
vector<long double> p, v;
/*
long double din(int pos, int ky, int kn){
    if(ky==0&&kn==0)return 1.0;
    if(pos>=p.size())return 0.0;
    if(ky<0||kn<0)return 0.0;
    long double aux1, aux2;
    aux1=p[pos]*din(pos+1, ky-1, kn) + (1.0-p[pos])*din(pos+1, ky, kn-1);
    aux2=din(pos+1, ky, kn);
    cout<<pos<<" "<<p[pos]<<" "<<" "<<ky<<" "<<kn<<endl;
    cout<<aux1<<" "<<aux2<<endl;
    return max(aux1, aux2);
}
*/

long double prob(int pos, int ky){
    //cout<<pos<<" "<<ky<<endl;
    if(ky==0&&pos==v.size())return 1.0;
    if(ky<0||v.size()-pos<ky)return 0.0;
    if(pos==v.size())return 0.0;
    return v[pos]*prob(pos+1, ky-1) + (1.0-v[pos])*prob(pos+1, ky);
}

int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int cases,t,n,i,a,c,j,k;
    double aux,aux2;
    scanf("%d",&cases);
    for(t=1;t<=cases;t++){
        p.clear();
        v.clear();
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++){
            scanf("%lf", &aux);
            p.push_back(aux);
        }
        //sort(p.begin(), p.end());
        //aux = din(0, k/2, k/2);
        aux = 0;
        for(i=0;i<(1<<n);i++){
            a=i;
            c=0;
            while(a>0){
                c+=(a%2);
                a/=2;
            }
            if(c!=k)continue;
            v.clear();
            a=i;
            j=0;
            while(a>0){
                if(a%2==1){
                    v.push_back(p[j]);
                }
                a/=2;
                j++;
            }
            aux2=prob(0, k/2);
            if(aux<aux2)aux=aux2;
        }
        //for(i=0;i<v.size();i++)cout<<"HOLI"<<v[i]<<endl;
        printf("Case #%d: %.8lf\n",t,aux);
    }
}

