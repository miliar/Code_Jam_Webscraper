# include <cstdio>
# include <iostream>
using namespace std;

int getMinTime (int *A, int sz, int time){
    int val=-1, id=-1, t1, t2;;
    for (int i=0; i<sz; i++){
        if (val<=A[i]){
            id = i;
            val = A[i];
        }
    }
    if (val<4) return (val+time);
    else if (val==4){
        A[id] = 2;
        A[sz] = 2;
        t1 = getMinTime(A, sz+1, time+1);
        A[id] = val;
        A[sz] = 0;
        return min(val+time, t1);
    }
    else if (val<8){
        A[id] = 3;
        A[sz] = val-3;
        t1 = getMinTime(A, sz+1, time+1);
        A[id] = val;
        A[sz] = 0;
        return min(val+time, t1);
    }
    else if (val==8){
        A[id] = 4;
        A[sz] = 4;
        t1 = getMinTime(A, sz+1, time+1);
        A[id] = val;
        A[sz] = 0;
        return min(val+time, t1);
    }
    else{
        A[id] = 3;
        A[sz] = 6;
        t1 = getMinTime(A, sz+1, time+1);
        A[id] = 4;
        A[sz] = 5;
        t2 = getMinTime(A, sz+1, time+1);
        A[id] = val;
        A[sz] = 0;
        return min((val+time), min(t1, t2));
    }
}

int main(){
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("Bout.txt", "w", stdout);
    int A[1000], d, p, cases, caseno=0, t, i;
    scanf ("%d", &cases);
    while (cases--){
        for (i=0; i<1000; i++) A[i] = 0;
        scanf ("%d", &d);
        for (i=0; i<d; i++){
            scanf ("%d", &A[i]);
        }
        t = getMinTime (A, d, 0);
        printf ("Case #%d: %d\n", ++caseno, t);
    }
    return 0;
}
