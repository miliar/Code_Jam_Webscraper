#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int n;
int m;
int zip[150];
string zips[150];
bool path[150][150];
bool visited[150];
string best;
int parent[150];

bool less1(string x)
{
    for (int i = 0; i < x.length(); i++) {
        if (x[i] > best[i]) {
            return false;
        } else {
            if (x[i] < best[i]) {
                return true;
            }
        }
    }
}

void recursion(int on, string test, int beento)
{
    //cout << "AT " << on << endl;
    //cout << beento << endl;
    if (beento == n) {
        //cout << test << endl;
        if (best == "") {
            best = test;
        } else {
            if (less1(test)) {
                best = test;
            }
        }
    } else {
        if (parent[on] != -1) {
            recursion(parent[on], test, beento);
        }
        int lowest = 999999;
        int go = -1;
        for (int i = 0; i < n; i++) {
            if (visited[i] == false) {
                if (path[on][i]) {
                    if (zip[i] < lowest) {
                        lowest = zip[i];
                        go = i;
                    }
                }
            }
        }
        if (go >= 0) {
            visited[go] = true;
            parent[go] = on;
            recursion(go, test + zips[go], beento + 1);
            parent[go] = -1;
            visited[go] = false;
        }
    }
}

void tostr()
{
    char buffer[5];
    for (int i = 0; i < n; i++) {
        itoa(zip[i], buffer, 10);
        string x = "     ";
        x[0] = buffer[0];
        x[1] = buffer[1];
        x[2] = buffer[2];
        x[3] = buffer[3];
        x[4] = buffer[4];
        zips[i] = x;
    }
}

void search(int startn)
{
    for (int i = 0; i < n; i++) {
        visited[i] = false;
        parent[i] = -1;
    }
    visited[startn] = true;
    int lowest = 199999;
    int got2;
    for (int i = 0; i < n; i++) {
        if (path[startn][i]) {
            if (zip[i] < lowest) {
                lowest = zip[i];
                got2 = i;
            }
        }
    }
    string test = zips[startn] + zips[got2];
    parent[got2] = startn;
    visited[got2] = true;
    recursion(got2, test, 2);
}

int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    int t;
    input >> t;
    int h, j;
    for (int i = 0; i < t; i++) {
        input >> n >> m;
        int lowest = 99999;
        int start;
        for (int x = 0; x < n; x++) {
            input >> zip[x];
            if (zip[x] <= lowest) {
                lowest = zip[x];
                start = x;
            }
            for (int y = 0; y < n; y++) {
                path[x][y] = false;
            }
        }
        for (int u = 0; u < m; u++) {
            input >> h >> j;
            path[h - 1][j - 1] = true;
            path[j - 1][h - 1] = true;
        }
        best = "";
        tostr();
        if (n > 1) {
            search(start);
            output << "Case #" << i + 1 << ": " << best << endl;
        } else {
            output << "Case #" << i + 1 << ": " << zip[0] << endl;
        }
    }
    return 0;
}
