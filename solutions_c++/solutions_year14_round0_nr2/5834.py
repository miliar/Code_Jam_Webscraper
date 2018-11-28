#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
using namespace std;

class Roundb {
public:
    Roundb(char* FileName);
    ~Roundb();
    void calc_time();
    int get_total(){return total;};
private:
    ifstream input;
    ofstream output;
    int total;
    int case_atual;
    double t1;
    double t2;
    double C;
    double F;
    double X;
    double rate;
    double sum (int n);
};

Roundb::Roundb(char* FileName) {
    input.open(FileName, ios::in);
    output.open("Output.txt", ios::out);
    input >> total;
    case_atual = 1;
    rate = 2.0;
}

Roundb::~Roundb(){
    input.close();
    output.close();
}

void Roundb::calc_time(){
    input >> C;
    input >> F;
    input >> X;

    int cont = 2;
    double rate_aux = rate;
    t1 = X / rate;

    rate_aux = rate + F;
    t2 = C / rate + X / rate_aux;

    while (t2 < t1) {
        t1 = t2;

        rate_aux = rate + cont * F;
        t2 = X / rate_aux;
        double sum_C = sum(cont);
        t2 += sum_C;

        cont++;
    }
    output << std::fixed;
    output << "Case #" << case_atual << ": "  << std::setprecision(7) << t1 << endl;
    case_atual++;
    total--;
}

double Roundb::sum(int n) {
    double aux = 0.0;
    double temp;
    for (int i = 0; i < n; i++) {
        temp = C / (rate + i * F);
        aux += temp;
    }
    return aux;
}

int main() {
Roundb roundb ("teste1.in");
while (roundb.get_total() > 0) {
    roundb.calc_time();
}
return 0;
}
