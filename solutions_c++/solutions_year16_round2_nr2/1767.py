#include <bits/stdc++.h>
#define ll long long
using namespace std;



string a,b;





struct Pair{
    string u,v;
    Pair(string uu,string vv){
        u = uu;
        v = vv;
    }
};



int str2int(string s) {
	stringstream ss(s);
	int x;
	ss >> x;
	return x;
}



Pair MIN(Pair a,Pair b){

    int a1 = str2int(a.u);
    int a2 = str2int(a.v);
    int b1 = str2int(b.u);
    int b2 = str2int(b.v);

    int aa = abs(a1-a2);
    int bb = abs(b1-b2);
    if(aa<bb){
        return a;
    }
    else if(aa>bb){
        return b;
    }
    else{
        if(a1<b1){
            return a;
        }
        else if(a1>b1){
            return b;
        }
        else{
            if(a2<b2){
                return a;
            }
            else{
                return b;
            }
        }
    }
}




Pair rec(string u,string v){


    string uu = u;string vv = v;
    Pair m = Pair("0000","9999");
    int ok = 0;
    for(int c = 0;c<uu.size();c++){
        if(uu[c] == '?'){
            ok = 1;
            for(char d = '0';d<='9';d++){
                uu[c] = d;
                m = MIN(rec(uu,vv),m);
            }
        }
    }
    for(int c = 0;c<vv.size();c++){
        if(vv[c] == '?'){
            ok = 1;
            for(char d = '0';d<='9';d++){
                vv[c] = d;
                m = MIN(rec(uu,vv),m);
            }
        }
    }

    if(ok){
        return m;
    }
    else{
        return Pair(u,v);
    }

}








int main(){
    //freopen("E:/B.in","r",stdin);
    //freopen("E:/bb.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int T = 1;
    while(t-->0){
        cin >> a >> b;
        Pair p = rec(a,b);
        printf("Case #%d: ",T++);
        cout << p.u <<" "<<p.v<< endl;
    }
    return 0;
}
