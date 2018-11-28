# include <bits/stdc++.h>
using namespace std;

char word[10500];
int mat[5][5];
void init();
void foundj();
void foundk();
int l,x,n;

vector <int> is;
vector <int> js;
vector <int> ks;


int mult(int a, int b){
    int pa = abs(a);
    int pb = abs(b);
    int ans = mat[pa][pb];
    if ( (a<0 && b>0) || (a>0 && b<0)   ){
        ans = -ans;
    }
    return ans;
}

void foundi(){
    int aux=1;
    for(int i=0 ; i<n ; i++){
        //cout<<word[i]<<" ";
        aux = mult(aux, int(word[i]-'g'));

        //cout<<aux<<endl;

        if(aux==2){
            is.push_back(i);
        }
    }
}

void foundj(){
    int aux,start;
    for(int j = 0 ; j<is.size() ; j++){

        start = is[j]+1;
        aux = 1;

        for(int i=start ; i<n ; i++){

            aux = mult(aux, int(word[i]-'g'));

            if(aux==3){
                js.push_back(i);
            }

        }

    }
}

void foundk(){
    int aux,start;
    for(int j = 0 ; j<js.size() ; j++){

        start = js[j]+1;
        aux = 1;

        for(int i=start ; i<n ; i++){
            aux = mult(aux, int(word[i]-'g'));
        }

        if(aux==4){
            ks.push_back(start);
            return;
        }

    }
}

int main(){
    //freopen("Cs.in","r",stdin);
    //freopen("C.out","w",stdout);
    init();
    int cases;
    cin>>cases;
    for(int h=1 ; h<=cases  ; h++){
        cin>>l>>x;
        n = l*x;
        char d;

        is.clear();
        js.clear();
        ks.clear();

        for(int i=0 ; i<l ; i++){
            cin>>d;
            for(int j=0 ; j<x ; j++){
                word[i+l*j]=d;
            }
        }

        foundi();
        foundj();
        foundk();


        /*for(int i=0 ; i<is.size() ; i++){
            cout<<is[i]<<" ";
        }cout<<endl;



        for(int i=0 ; i<js.size() ; i++){
            cout<<js[i]<<" ";
        }cout<<endl;



        for(int i=0 ; i<ks.size() ; i++){
            cout<<ks[i]<<" ";
        }cout<<endl;

        cout<<ks.size()<<endl;*/

        cout<<"Case #"<<h<<": ";
        if(ks.size()>=1){
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;
        }
    }
}

void init(){
    mat[1][1] = 1;
    mat[2][1] = 2;
    mat[3][1] = 3;
    mat[4][1] = 4;

    mat[1][2] = 2;
    mat[2][2] = -1;
    mat[3][2] = -4;
    mat[4][2] = 3;

    mat[1][3] = 3;
    mat[2][3] = 4;
    mat[3][3] = -1;
    mat[4][3] = -2;

    mat[1][4] = 4;
    mat[2][4] = -3;
    mat[3][4] = 2;
    mat[4][4] = -1;

}





