#include <iostream>
#include <algorithm>
using namespace std;

int n,i,j,m,sum,answer;
int c[1001];

int problem(){
    cin >> n;
    for(i=0;i<n;i++){
        cin >> c[i];
        m = max(m,c[i]);
    }
    answer = m;
    for(i=1;i<=m;i++){
        sum=0;
        for(j=0;j<n;j++){
            if(c[j]%i==0){
                sum += c[j]/i-1;
            } else {
                sum += c[j]/i;
            }
        }
        answer = min(answer,sum+i);
    }
    return answer;
}

int main(){
    int CASENO,TESTCASE;
    cin >> TESTCASE;
    for(CASENO=1;CASENO<=TESTCASE;CASENO++){
        cout << "Case #" << CASENO << ": " << problem() << endl;
    }
}
