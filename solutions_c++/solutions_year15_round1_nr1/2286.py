#include <fstream>
#include <string>
#include <map>
using namespace std;

int main(){
    int T;
    ifstream f("input.txt");
    ofstream w("output.txt");
    f>>T;
    for (int tests=0;tests<T;tests++)
    {
        long n;
        f>>n;
        int m[1001];
        for (int i=0;i<n;i++)
            f>>m[i];
        int speed=0;
        long long ans1=0;
        for (int i=0;i<n-1;i++){
            if (m[i+1]<m[i]) ans1+=m[i]-m[i+1];
            if (m[i]-m[i+1]>speed) speed=m[i]-m[i+1];
        }
        long long ans2=0;
        for (int i=0;i<n-1;i++){
              if (m[i]>speed) ans2+=speed; else ans2+=m[i];
         }


        w<<"Case #"<<(tests+1)<<": "<<ans1<<" "<<ans2<<endl;
    }
    f.close();
    w.close();


    return 0;
}


