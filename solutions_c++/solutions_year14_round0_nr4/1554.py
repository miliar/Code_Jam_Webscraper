#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

#include <set>

double Q = 0.000001;

typedef set<double> dset;
typedef dset::iterator ditr;
typedef dset::reverse_iterator dritr;

void printSet(dset &d)
{
    for (ditr it = d.begin(); it != d.end(); it++)
        printf("%f ", *it);
    
}

void offerD(double &told, double &real, dset &db, dset &opp)
{
    ditr it = db.begin();
    double b = *it;
    double bo = *opp.begin();
    double r = *opp.rbegin();
    if (b < bo)
    {
        told = r - Q;
    }
    else
    {
        told = r + Q;
    }
    
    real = b;
    db.erase(it);


    
}

double offer(dset &db)
{
    ditr it = db.begin();
    double r = *it;
    db.erase(it);
    return r;
}

double offer2(dset &db)
{
    dritr it = db.rbegin();
    double r = *it;
    db.erase(--(it.base()));
    return r;
}

double offer3(dset &db)
{
    int R = rand() % db.size();
    ditr it = db.begin();
    for (int i = 0; i < R; i++) it++;
    double r = *it;
    db.erase(it);
    return r;
}



double respond(double b, dset &db)
{
    ditr it = db.upper_bound(b);
    if (it == db.end())
    {
        it = db.begin();
    }
    double r = *it;
    db.erase(it);
    return r;
}

void processCase(int n) 
{
    int N;
    cin >> N;
    dset p1;
    dset p2;
    
    double d;
    for (int i = 0; i < N; i++)
    {
        cin >> d;
        p1.insert(d);
    }

    for (int i = 0; i < N; i++)
    {
        cin >> d;
        p2.insert(d);
    }

    dset u1(p1);
    dset u2(p2);


    int s1 = 0;

    for (int i = 0; i < N; i++)
    {
        double d1 = offer(p1);
        double d2 = respond(d1, p2);
        bool w = d1 > d2;
//        printf("%d: %f vs %f - %d\n", i, d1, d2, w);
        if (w)
            s1++;
    }

    int c1 = 0;

    for (int i = 0; i < N; i++)
    {
    
        double r, t;
        offerD(t, r, u1, u2);
        double d2 = respond(t, u2);
        bool w = r > d2;
//        printf("%d: %f (%f) vs %f - %d\n", i,t, r, d2, w);
        if (w)
            c1++;
    }

    printf("Case #%d: %d %d\n", n, c1, s1);
}

            


int main(int argc, char **argv)
{
 
    int N = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        processCase(i + 1);

    return 0;
}