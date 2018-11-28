#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int T,D,P;

multiset<int> st;

int get_max(){
    multiset<int>::iterator it;
    it=st.end();
    it--;
    return *it;
}

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    int i,k,x,res,aux,cnt;
    for (k=1; k<=T; k++){
        fout << "Case #" << k << ": ";
        fin >> D;

        for (i=1; i<=D; i++){
            fin >> x;
            st.insert(x);
        }
        res=get_max();
        cnt=0;
        multiset<int>::iterator it;
        while (get_max()!=1){
            cnt++;
            it=st.end(); --it;
            aux=*it;
            st.erase(it);
            if (aux%2==0) st.insert(aux/2), st.insert(aux-aux/2);
            else{
                if ((aux/2)%2==0) st.insert(aux/2-1),st.insert(aux/2+1);
                else st.insert(aux/2),st.insert(aux-aux/2);
            }

            res=min(res,cnt+get_max());
        }

        st.clear();
        fout << res << "\n";
    }
    return 0;
}
