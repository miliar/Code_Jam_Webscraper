//
//  main.cpp
//  Pro1
//
//  Created by dong on 5/8/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>
#include <stdio.h>

#define MAX_PARTY 26

struct node {
    char label;
    int count;
public:
    node(){}
    node(char l, int c):label(l),count(c){}
};

class Heap {
    node data[MAX_PARTY+7];
    int length;
    
    void down(int i) {
        node tmp = data[i];
        int flag;
        while (i * 2 <= length) {
            flag = i * 2;
            if (flag + 1 <= length && data[flag+1].count > data[flag].count) {
                ++flag;
            }
            if (data[i].count > data[flag].count) {
                break;
            }
            data[i] = data[flag];
            i = flag;
        }
        data[i] = tmp;
    }
    
    void up(int i) {
        node tmp = data[i];
        while (i / 2 >= 1) {
            if (data[i/2].count > data[i].count) {
                break;
            }
            data[i] = data[i/2];
            i /= 2;
        }
        data[i] = tmp;
    }
    
public:
    Heap():length(0){}
    int size() {return length;}
    void push(node n) {
        data[++length] = n;
        up(length);
    }
    
    node pop() {
        node tmp = data[1];
        if (length > 1) {
            data[1] = data[length];
            --length;
            down(1);
        } else {
            --length;
        }
        return tmp;
    }
    
    node top() {
        return data[1];
    }
    
    void print(FILE *fout) {
        for (int i = 1; i <= length; ++i) {
            fprintf(fout, "\n%c %d\n", data[i].label, data[i].count);
        }
    }
};

int main(int argc, const char * argv[]) {
    FILE *fin = fopen("A-small-attempt0.in.txt", "r");
    FILE *fout = fopen("A-small-attempt0.out.txt", "w");
    
    int T, N, P;
    fscanf(fin, "%d", &T);
    fgetc(fin);
    
    Heap myheap;
    node n1, n2;
    for (int t = 1; t <= T; ++t) {
        fscanf(fin, "%d", &N);
        fgetc(fin);
        for (int i = 0; i < N; ++i) {
            fscanf(fin, "%d", &P);
            myheap.push(node((char)('A' + i), P));
        }
        //myheap.print(fout);
        fgetc(fin);
        fprintf(fout, "Case #%d:", t);
        while (myheap.size() > 0) {
            if (myheap.top().count > 1) {
                n1 = myheap.pop();
                n2 = myheap.pop();
                --n1.count;
                --n2.count;
                fprintf(fout, " %c%c", n1.label, n2.label);
                if (n1.count > 0) {myheap.push(n1);}
                if (n2.count > 0) {myheap.push(n2);}
            } else {
                if (myheap.size() != 3) {
                    n1 = myheap.pop();
                    n2 = myheap.pop();
                    --n1.count;
                    --n2.count;
                    fprintf(fout, " %c%c", n1.label, n2.label);
                    if (n1.count > 0) {myheap.push(n1);}
                    if (n2.count > 0) {myheap.push(n2);}
                } else {
                    n1 = myheap.pop();
                    --n1.count;
                    fprintf(fout, " %c", n1.label);
                    if (n1.count > 0) {myheap.push(n1);}
                }
            }
            //myheap.print(fout);
        }
        fprintf(fout, "\n");
    }
    
    fclose(fin);
    fclose(fout);
    
    return 0;
}
