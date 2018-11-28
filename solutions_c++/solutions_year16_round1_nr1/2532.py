bool onlyonecase=false;
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include "math.h"
#include <stdexcept>
#include <iostream>
#include <fstream>
#include <array>
#include <vector>
#include <deque>
#include <list>
#include <forward_list> 
#include <set>
#include <map>
#include <unordered_set> 
#include <unordered_map> 
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iterator>
#include <functional>
#include <cstdlib>
#include <string.h>
#include <sstream>

// Useful constants
#define INF                         (t)1e19
#define EPS                         1e-9
// Useful hardware instructions
#define bitcount                    __builtin_popcount
#define gcd                         __gcd
// Useful container manipulation / traversal macros
#define forall(i,a,b)               for (auto i=a;i!=b;i=(a<b)?i+1:i-1 )
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define IMPOSSIBLE "IMPOSSIBLE"

using namespace std;
istream * pin;

//typedef uintmax_t t;
typedef intmax_t t;

t konstansmod=(1e9)+7;

template<typename T>
vector<T> read(int num=-1,int szorzo=1,istream & in=*pin)
{
    vector<T> container;
    if (num==-1)
        in>>num;
    num*=szorzo;
    for (int i=0;i<num;i++)
    {
        T q;
        in>>q;
        container.push_back(q);
    }
    return container;
}


struct printer
{
ostream *o;
printer(ostream &a=cout):o(&a)
{

}

void pr()
{
*o<<"\n";
}

template<typename T>
void pr(T t)
{
*o<<fixed<<std::setprecision(9) << t<<"\n";
}

template<typename T>
void pr(vector<T> t)
{
    for(T w:t)
pr(w);
pr();
}

template<typename T, typename... Args>
void pr(T value, Args... args)
{
//cout<<value;
    pr(value);
pr(args...);
}

};
#define p(args...)  do { printer().pr(args); } while (false)
#ifdef DEBUG
#define dl(...) do {show(std::cerr, "Line", __LINE__);show(std::cerr, #__VA_ARGS__, __VA_ARGS__);} while (false)
#define d(...) do { show(std::cerr, #__VA_ARGS__, __VA_ARGS__); } while (false)
#else
#define dl(...) {}
#define d(...) {}
#endif

template<typename H1>
void show(std::ostream& out, const char* label, H1&& value) {
  //out << label << "=" << std::forward<H1>(value) << '\n';
// printer(out).pr(label+"=").pr(value);
out << label << "=" ;
printer(out).pr(value);
}

template<typename H1, typename ...T>
void show(std::ostream& out, const char* label, H1&& value, T&&... rest) {
  const char* pcomma = strchr(label, ',');
out.write(label, pcomma - label) << "=";
printer(out).pr(value);

 show(out,pcomma+1,std::forward<T>(rest)...);
}

void print(bool b)
{
    cout<<(b?"Yes":"No")<<"\n";
}

vector<double> gauss(vector< vector<double> > A) {
    int n = A.size();

    for (int i=0; i<n; i++) {
        // Search for maximum in this column
        double maxEl = abs(A[i][i]);
        int maxRow = i;
        for (int k=i+1; k<n; k++) {
            if (abs(A[k][i]) > maxEl) {
                maxEl = abs(A[k][i]);
                maxRow = k;
            }
        }

        // Swap maximum row with current row (column by column)
        for (int k=i; k<n+1;k++) {
            double tmp = A[maxRow][k];
            A[maxRow][k] = A[i][k];
            A[i][k] = tmp;
        }

        // Make all rows below this one 0 in current column
        for (int k=i+1; k<n; k++) {
            double c = -A[k][i]/A[i][i];
            for (int j=i; j<n+1; j++) {
                if (i==j) {
                    A[k][j] = 0;
                } else {
                    A[k][j] += c * A[i][j];
                }
            }
        }
    }

    // Solve equation Ax=b for an upper triangular matrix A
    vector<double> x(n);
    for (int i=n-1; i>=0; i--) {
        x[i] = A[i][n]/A[i][i];
        for (int k=i-1;k>=0; k--) {
            A[k][n] -= A[k][i] * x[i];
        }
    }
    return x;
}

void solve();
int main(int argc, char** argv) {
    srand((unsigned) time(NULL));
    ifstream * argfile=NULL;
    string filename="";
    if (argc>=2 && filename.length()==0)
        filename=argv[1];
    if (filename.length()>0)
    {
        argfile=new ifstream(filename);
        if (!argfile->is_open()) {
            cerr<<"file cant be opened,exiting. Filename:"<<filename<<"\n";
            cerr << "Error: " << strerror(errno)<<"\n";
            return 1;
        }
    }
    if (argfile) std::cin.rdbuf(argfile->rdbuf());
    istream & myfile=argfile?*argfile:cin;
    pin=&myfile;
    int num;
    if (onlyonecase)
    {
    solve(); return 0;
    }

    myfile>>num;
    for (int i = 0; i < num; i++) {
        cout<<"Case #"<<(i+1)<<": ";
        solve();
    }
    return 0;
}

void solve()
{
string q;
cin>>q;
string q2=q.substr(0,1);
for (int i=1;i<q.length();i++)
{
    //d(q,q2);
string a=q[i]+q2;
string b=q2+q[i];
if (a<b)
{
q2=b;
}
else
{
    q2=a;
}



}
p(q2);




}


