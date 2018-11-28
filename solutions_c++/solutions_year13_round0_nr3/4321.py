#include <bits/stdc++.h>
#define f(i,x,y) for (int i = int(x); i < int(y); i++)
#define fd(i,x,y) for(int i = int(x); i>= int(y); i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define oo (1<<30)

using namespace std;
/*
bool ispal(ll num){
    string cad;
    while(num>0){
        int dig = num%10;
        num/=10;
        cad+='0'+dig;
    }
    f(i,0,cad.size()){
        if(cad[i]!=cad[cad.size()-i-1]) return 0;
    }
    return 1;
}

ll vol(ll num){
    ll nuevo=0;
    while(num>0){
        int dig = num%10;
        num/=10;
        nuevo=(nuevo*10) + dig;
    }
    return nuevo;
}*/

int main(){
    freopen("in.c","r",stdin);
    freopen("out.c","w",stdout);
    //preprocesa
    /*ll pot[1000];
    pot[0]=1;
    f(i,1,20){
        pot[i] = pot[i-1]*10;
    }
    //vamos a ver con la mitad de digitos
    vector<ll> ans;
    ans.pb(1);
    ans.pb(4);
    ans.pb(9);
    f(i,2,18){
        if((i%2)==0){
            //cout<<"es parrrrrrr------------------------------ "<<i<<endl;
            for(ll j = pot[(i/2)-1]; j < pot[(i/2)] ; j++){
                ll num = j*pot[i/2]+vol(j);
                double cuad = sqrt(num);
                //cout<<"-->"<<num<<endl;
                if( ((ll)cuad*(ll)cuad)==num    &&   ispal((ll) cuad) ){//vemos si es un cuadrado perfecto

                    ans.pb(num);
                }
            }
        }else{
            //cout<<"es imparrrrrrr------------------------------ "<<i<<endl;
            for(ll j = pot[(i/2) - 1]; j< pot[(i/2)] ; j++){
                f(k,0,10){
                    ll num = j*10 + k;
                    num = num*pot[i/2] + vol(j);
                    double cuad = sqrt(num);
                    if( ((ll)cuad*(ll)cuad)==num && ispal((ll) cuad)){//vemos si es un cuadrado perfecto
                        ans.pb(num);

                    }
                }
            }
        }
    }

    f(i,0,ans.size()){
        cout<<ans[i]<<" ";
    }
    cout<<endl;*/
    ll preproc[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401,
     121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001,
      1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321,
       1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121,
        123212464212321 ,123456787654321 ,400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001,
        10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121,
         12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121 ,12321024642012321, 12323244744232321, 12343456865434321,
          12345678987654321, 40000000800000004, 40004000900040004,0,0,0,0,0,0,0,0,0,0};

//tiene 70 numeros
    int TC,NC=1;
    ll a , b;
    scanf("%d",&TC);
    while(TC--){
        scanf("%lld%lld",&a,&b);
        int ind1,ind2;
        ind1 = 70;
        f(i,0,70){
            if(preproc[i]>=a){
                    if(preproc[i]>=a)
                    ind1 = i;
                    else
                    ind1 = i-1;
                break;
            }
        }
        ind2 = 70;
        f(i,0,70){
            if(preproc[i]>b){
                ind2 = i;
                break;
            }
        }
        //cout<<ind1<<" "<<ind2<<endl;
        printf("Case #%d: %d\n",NC++,ind2-ind1);

    }
    return 0;
}

