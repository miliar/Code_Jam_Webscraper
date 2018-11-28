#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

void quicksort(double array[], int lefti , int righti)
{
    double pivot = array[(lefti + righti)/2];
    //cout << "Quicksort " << lefti << " and " << righti << " and pivot : " << pivot << endl;
    int originall = lefti;
    int originalr = righti;
    while (lefti <= righti) {
        while (array[lefti] < pivot) {
            lefti++;
        }
        while (array[righti] > pivot) {
            righti--;
        }
        if (lefti <= righti) {
            //cout << "Swap " << array[lefti] << " with " << array[righti] << endl;
            double n;
            n = array[lefti];
            array[lefti] = array[righti];
            array[righti] = n;
            lefti++;
            righti--;
        }
    }
    if (originall < righti) {
        quicksort(array, originall , righti);
    }
    if (lefti < originalr) {
        quicksort(array, lefti , originalr);
    }
}

int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    int t;
    input >> t;
    double nao[1000];
    double ken[1000];
    for (int i = 0; i < t; i++) {
        int n;
        input >> n;
        for (int x = 0; x < n; x++) {
            input >> nao[x];
        }
        for (int x = 0; x < n; x++) {
            input >> ken[x];
        }
        quicksort(nao, 0, n - 1);
        quicksort(ken, 0, n - 1);
        int startken = n - 1;
        int startnoa = n - 1;
        int pointsnao = 0;
        //output << "Sorted Nao : " << endl;
        for (int o = 0; o < n; o++) {
           //output << nao[o] << " ";
        }
        //output << endl << "Sorted Ken : " << endl;
        for (int o = 0; o < n; o++) {
            //output << ken[o] << " ";
        }
        //output << endl;
        int pointsnao2 = 0;
        for (int o = 0; o < n; o++) {
            if (nao[startnoa] > ken[startken]) {
                pointsnao++;
                startken--;
                startnoa--;
            } else {
                startken--;
            }
        }
        startken = n - 1;
        startnoa = n - 1;
        for (int o = 0; o < n; o++) {
            if (nao[startnoa] > ken[startken]) {
                pointsnao2++;
                startnoa--;
            } else {
                startken--;
                startnoa--;
            }
        }
        output << "Case #" << i + 1 << ": " << pointsnao << " " << pointsnao2 << endl;
    }
    return 0;
}
