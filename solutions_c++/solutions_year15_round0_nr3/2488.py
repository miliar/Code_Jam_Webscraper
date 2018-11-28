#include <iostream>
#include <vector>
using namespace std;

#define I 2
#define J 3
#define K 4

int ctc(char v);



int table[4][4] =
        {
                { 1 , I , J , K },
                { I ,-1 , K ,-J },
                { J ,-K ,-1 , I },
                { K , J ,-I ,-1 }
        };



int mult(int a,int b){

    int aa = abs(a); //we use absolute for matrix
    int ab = abs(b);

    int sa,sb;

    if (aa != 0) { sa = a / aa; }else{ sa = 1; };  //we get a sign
    if (ab != 0) { sb = b / ab; }else{ sb = 1; };  //we get b sign

    int value = table[aa - 1][ab - 1]; //we get the absolute value

    return value * sa * sb;
}
vector <int> stc(string code){
    vector <int> answer;
    for (int x = 0;x < code.size();x++){
        if (code[x] == 'i'){ answer.push_back(I); }
        if (code[x] == 'j'){ answer.push_back(J); }
        if (code[x] == 'k'){ answer.push_back(K); }
    }
    return answer;
}
int ctc(char v){
    if (v == 'i'){ return I; }
    if (v == 'j'){ return J; }
    if (v == 'k'){ return K; }
}

void Solve(int x);

int main() {
    freopen("input2.in","r",stdin);
    freopen("output.out","w+",stdout);

    int T; cin>>T;
    for (int x = 1;x <= T ;x++){
        Solve(x);
    }
}
vector <int> Optimizar(vector <int> sw){

    vector <int> result;
    bool start = true;
    int factor = sw[0];
    for (int x = 0;x < sw.size();x++){
        if (start){
            factor = sw[x];
            start = false;
        }else{
            factor = mult(factor,ctc(sw[x]));
        }
        if (factor == I or factor == J or factor == K) {
            result.push_back(factor);
            start = true;
        }else if(factor == 1){ //no lo tenemos en cuenta porque no influye
            start = true;
        }else if(x == sw.size() - 1){
            result.push_back(factor);
        }
    }

    return result;
}
void Productos(vector <int> value){
    vector <int> result;

    for (int x = value.size()-1;x > -1;x--){

    }
}
void Solve(int x){
    cout<<"Case #"<<x<<": ";
    int L,X; cin>>L>>X; //longitud, repeticion de la cadena

    string sw; cin>>sw;
    //cout<<sw<<endl;


    /** Decodificamos sw **/
    vector <int> value = stc(sw);
    vector <int> result = Optimizar(value);
    vector <int> total;

    for (int r = 0;r < X;r++){ //por cada repeticion
        for (int i = 0;i < result.size();i++){
            total.push_back(result[i]);
        }
    }
    Optimizar(total);

    /*for (int x = 0;x < total.size();x++){
        cout<<total[x];
    }
    cout<<endl;/*/

    if (total.size() < 3){
        cout<<"NO"<<endl;
        return;
    }

    int factor = total[0];

    for (int a = 0;a < total.size();a++){
        if (a != 0){ factor = mult(factor,total[a]); }
    }
    if (factor != -1){
        cout<<"NO"<<endl;
        return;
    }

    factor = total[0];
    for (int a = 0;a < total.size() - 2;a++){

        if (a != 0){ factor = mult(factor,total[a]); }

        if (factor == I){ //si encontramos una K
            int factorB = total[a + 1];
            for (int b = a + 1;b < total.size() - 1;b++){
                if (b != a + 1){ factorB = mult(factorB,total[b]); }

                if (factorB == J){
                    int factorC = total[b + 1];
                    for (int c = b + 1;c < total.size();c++){
                        if (c != b + 1){ factorC = mult(factorC,total[c]); }
                    }
                    if (factorC == K){
                        cout<<"YES"<<endl;
                        return;
                    }
                }
            }
        }
    }
    cout<<"NO"<<endl;
    return;
    //En result tenemos hecha una optimizacion de la cadena

}