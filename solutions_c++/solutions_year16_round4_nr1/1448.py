#include <iostream>
#include <string>
#include <cassert>

using namespace std;

string busca(int N, int P, int R, int S) {
    if ((N!=(P+R+S)) || (P<0) || (R<0) || (S<0)) {
        assert(0);
    }
    if (N==1) {
        if (P>0) {
            return "P";
        }
        if (R>0) {
            return "R";
        }
        if (S>0) {
            return "S";
        }
    }
    int H = N>>1;
    if (P>H) {
        return "IMPOSSIBLE";
    }
    int RS = H - P;
    int PR = R-RS;
    int PS = S-RS;
    if (PR<0) {
        return "IMPOSSIBLE";
    }
    if (PS<0) {
        return "IMPOSSIBLE";
    }
    string anterior = busca(H, PR, RS, PS);
    if (anterior == "IMPOSSIBLE") {
        return anterior;
    }
    string resultado = "";
    if (anterior.length()!=H) {
        assert(0);
    }
    for (int i=0;i<H;i++) {
        if (anterior[i]=='P') {
            resultado = resultado + "PR";
            PR--;
        }
        else if (anterior[i]=='R') {
            resultado = resultado + "RS";
            RS--;
        }
        else if (anterior[i]=='S') {
            resultado = resultado + "PS";
            PS--;
        }
        else {
            assert(0);
        }
    }
    if ((PR!=0)||(PS!=0)||(RS!=0))
        assert(0);
    return resultado;
}

string ordena(const string &r) {
    if (r=="IMPOSSIBLE")
        return r;
    if (r.length()==1)
        return r;
    unsigned int H=r.length()>>1;
    string izquierda=ordena(r.substr(0, H));
    string derecha = ordena(r.substr(H, H));
    string resultado = izquierda+derecha;
    string volteado = derecha + izquierda;
    if (volteado<resultado)
        resultado = volteado;
    //cerr << "  " << resultado << endl;
    return resultado;
}

int main()
{
    int T;
    cin >> T;
    //cerr << "T:" << T << '\n';
    for (int t=1;t<=T;t++) {
        int N, R, P, S;
        cin >> N;
        cin >> R;
        cin >> P;
        cin >> S;
        N = 1<<N;
        //cerr << N << " " << R << " " <<  P << " " <<  S << endl;
        string resultado = ordena(busca(N, P, R, S));
        cout << "Case #" << t << ": " << resultado << endl;
    }
    return 0;
}
