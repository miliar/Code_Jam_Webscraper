#include <iostream>
#include <fstream>

#define array_s 100

using namespace std;

ifstream f("A-large.in");
ofstream g("A-large.out");

int nr[array_s];
int buff[array_s];

void mutiply(int mul)
{
    int tr = 0;
    for(int i=array_s - 1; i>=0; i--) {
        nr[i] = nr[i] * mul + tr;
        if (nr[i] >= 10) {
            tr = nr[i] / 10;
            nr[i] = nr[i] % 10;
        } else {
            tr = 0;
        }
    }
}

void add()
{
    int tr = 0;
    for(int i=array_s - 1; i>=0; i--) {
        nr[i] = nr[i] + buff[i] + tr;
        if (nr[i] >= 10) {
            tr = nr[i] / 10;
            nr[i] = nr[i] % 10;
        } else {
            tr = 0;
        }
    }
}

void read() {
    int n, step = 1;
    f>>n;
    while(n > 0) {
        nr[array_s-step] = n%10;
        buff[array_s-step] = n%10;
        n/=10;
        step++;
    }
}

void print() {
    bool print = false;
    for(int i=0; i<array_s; i++) {
        if(nr[i] != 0 && !print) {
            print = true;
        }

        if (print) {
            g<<nr[i];
        }
    }

    if(!print) {
        g<<0;
    }
}

int count[10];
bool checkIfSleeps() {
    bool print = false;

    for(int i=0; i<array_s; i++) {
        if(nr[i] != 0 && !print) {
            print = true;
        }

        if (print) {
            count[nr[i]%10]++;
        }
    }

    for(int i=0; i<10; i++) {
        if(count[i] == 0) {
            return false;
        }
    }
    return true;
}

void resetarray() {
    for(int i = 0; i< array_s; i++) {
        nr[i] = 0;
        buff[i] = 0;
    }
    for(int i = 0; i< 10; i++) {
        count[i] = 0;
    }
}

int main()
{
    int t; f>>t;

    for (int i = 0; i<t; i++) {
        resetarray();
        read();

        int step = 0;
        while(!checkIfSleeps() && step < 100) {
            add();
            step ++;
        }
        g<<"Case #"<<i+1<<": ";

        if (step == 100) {
            g<<"INSOMNIA\n";
        } else {
            print();
            g<<"\n";
        }
    }

    f.close();
    g.close();
    return 0;
}
