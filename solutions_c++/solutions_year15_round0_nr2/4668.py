#include <iostream>
using namespace std;
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
int arr[1010];
int temp[1010];
int an1;

int min(int a, int b) {
    return a > b ? b : a;
}

int cal(int start, int allow) {
    if (start > 4) {
        int a = (start-1) / 3;
        int b = start %3;
        arr[3] += (arr[start] * a);
        if (b != 0)
            arr[b] += (arr[start]);
        
        int i= start -1;
        while(arr[i] == 0) {
            i --;
        }
        
        int ret = cal(i, allow);
        
        //cout<<"start is :"<<start<<" and ret is:"<<ret<<endl;
        return min(start, ret + arr[start] * a);
        
    } else if (start == 4){
        if (arr[3] == 0) {
            return min(4, 2 + arr[4]);
        } else {
            return 4;
        }
    } else {
        return start;
    }
}


int cal1(int start, int allow) {
    if (allow <= 0) {
        return -1;
    }
    
    if (start == 1)
        return 1;
    
    int a = start /2;
    int b = start /2 + 1;
    
    arr[a] += arr[start];
    if (start %2 == 0)
        arr[a] += arr[start];
    else
        arr[b] += arr[start];
    
    int i = start - 1;
    while(arr[i] == 0) {
        i --;
    }
    int ret = cal1(i, allow - arr[start]);
    //cout<<"start:"<<start<<" ret:"<<ret<<" i:"<<i<<endl;
    if(ret < 0) {
        if (start > allow)
            return -1;
        else
            return start;
    } else {
        int min = start;
        if (ret + arr[start] < min) {
            min = ret + arr[start];
        }
        if (min > allow)
            return -1;
        else
            return min;
    }
    
    
}

void process() {
    int i,j;
    i = 1000;
    while(arr[i] == 0) {
        i--;
        
    }
    
    an1 = cal(i, i);
    
    j=1000;
    for(;j>=0;j--) {
        arr[j] = temp[j];
    }
    
    int an2 = cal1(i, i);
    
    //cout<<"i:"<<i<<" an1:"<<an1<<" an2:"<<an2<<endl;
    an1 = min(an1, an2);
}

int main() {
    CASET {
        an1 = 0;
        
        int d;
        cin>>d;
        memset(arr, 0, sizeof(arr));
        memset(temp, 0, sizeof(temp));
        
        //cout<<d<<endl;
        int i,j;
        for(i=0;i<d;i++) {
            cin>>j;
            arr[j] ++;
            temp[j]++;
        }
        
        process();
        
        printf("Case #%d: %d\n",case_n++,an1);
    }
}