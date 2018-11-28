#include <iostream>
#include <set>
using namespace std;

bool all(set<int> myset){
    bool output = true;
    for (int i=0;i<10;i++){
        if (myset.find(i)!=myset.end()){
           output *= true;
        }
        else{
            return false;
        }
    }
    return output;
}

void digits(long val, set<int> & myset){
    int rem;
    while (val!=0){
        rem = val % 10;
        myset.insert(rem);
        val = val / 10;
    }
}

long get_sleep_time(long n){
    std::set<int> myset;
    long step = 0;
    long val = n;
    while (!all(myset)){
        val = step*n+n;
        digits(val,myset);
        step++;
        /*cout << step << " -  " ;
        for (set<int>::iterator it=myset.begin(); it!=myset.end(); ++it){
           cout << *it << " ";
        }
        cout << endl;
        */
        if (step > (n+1)*1000){
            return -1;
        }
    }
    return val;
};


int main() {
    long T,n;
    long t;
    cin >> T;
    for (long i=0;i<T;i++){
        cin >> n;
        t = get_sleep_time(n);
        if (t>0) {
            cout << "CASE #" << i+1 << ": " << t <<endl;
        }
        else {
            cout << "CASE #" << i+1 << ": INSOMNIA" <<endl;
        }
    }

    return 0;
}