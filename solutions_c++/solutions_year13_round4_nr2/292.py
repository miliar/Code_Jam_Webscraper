#include<iostream>

const int MAXN = 51;

int n;
long long p;
long long total;
int a[MAXN];
long long c[MAXN];

bool check1(long long x){
    long long AA = x;
    long long BB = total-1-x;
    for (int i=0;i<n;++i){
        if (a[i]==1){//lose
            AA = (AA-1)/2;
            BB = c[i]-1-AA;
        } else {
            if (AA>0){
                return false;
            }
            BB /= 2;
        }
    }
    return true;
}
long long work1(){
    long long low = 0;
    long long high = total-1;
    while (low<high){
        long long mid = (low+high+1)/2;
        if (!check1(mid)){
            high = mid-1;
        } else {
            low = mid;
        }
    }
    return low;
}
bool check2(long long x){
    long long BB = total-1-x;
    long long tmp = 0;
    for (int i=0;i<n;++i){
        if (BB>0){
            tmp += c[i];
        }
        BB = (BB-1)/2;
    }
    return tmp>=total-p;
}
long long work2(){
    long long low = 0;
    long long high = total-1;
    while (low<high){
        long long mid = (low+high+1)/2;
        if (check2(mid)){
            low = mid;
        } else {
            high = mid-1;
        }
    }
    return low;
}

int main(int argc,char* argv[]){
    //freopen("input.txt","r",stdin);
    int noc;
    std::cin >> noc;
    for (int tnoc=1;tnoc<=noc;++tnoc){
        std::cin >> n >> p;
        total = 1;
        long long tmp = p-1;
        for (int i=n-1;i>=0;--i){
            a[i] = tmp%2;
            tmp /= 2;
            c[i] = total;
            total *= 2;
        }
        long long res1 = work1();
        long long res2 = work2();
        
        std::cout << "Case #" << tnoc <<": "<< res1 << " " << res2 << std::endl;
    }

    return 0;
}
