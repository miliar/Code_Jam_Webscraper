#include <bits/stdc++.h>

using namespace std;

int main() {
    string infile, outfile;
    cin>>infile;
    outfile = infile + ".out";

    ifstream in(infile.c_str());
    ofstream out(outfile.c_str());
//    ifstream& in = (file == "std" ? cin : *(new ifstream(file.c_str());
/*    FILE* in = NULL, *out = NULL;
    if (file != "std") {
        in = fopen(file.c_str(), "r");
        file += ".out";
        out = fopen(file.c_str(), "w");
    }
    else {
        in = stdin;
        out = stdout;
    }
*/
//    cout<<1.1<<endl;
    int T;
//    fscanf(in, "%d", &T);
    in>>T;
    for (int cas = 1; cas <= T; ++cas) {
        double C, F, X;
//        fscanf(in, "%f%f%f", &C, &F, &X);
        in>>C>>F>>X;

//        out<<C<<" ,"<<F<<" , "<<X<<endl;

 //       printf("(%.3f %.3f %.3f)\n", C, F, X);

        int max_n = 0;
        double x = (F * X / C - 2 - F) / F;
        if (x <= 0) max_n = 2;
        else max_n = int(ceil(x) + 2);

//        cout<<"maxn = "<<max_n<<endl;
        double min_time = X / 2, t = X / 2;

        out<<"Case #"<<cas<<": ";
        for (int n = 0; n <= max_n; ++n) {
            double delta = C / (2 + n * F) + X / (2 + (n + 1) * F) - X / (2 + n * F);
            t += delta;
  //          cout<<"delta = "<<delta<<"new_t = "<<t<<endl;
            min_time = min(min_time, t);
        }
        char str[128];
//        fprintf(out, "%.7f\n", min_time);
        snprintf(str, 128, "%.9f", min_time);
        out<<str<<endl;
    }

/*
    if (file != "std") {
        fclose(in), fclose(out);
    }
*/
    getchar();
    return 0;
}
