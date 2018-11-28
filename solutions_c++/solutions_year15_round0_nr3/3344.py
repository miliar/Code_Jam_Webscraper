 #include <bits/stdc++.h>
 using namespace std;

 string arreglo[100000];

 string  f(string a, char b)
 {
     if(a == "1" && b=='1') return "1";
     if(a == "1" && b=='i') return "i";
     if(a == "1" && b=='j') return "j";
     if(a == "1" && b=='k') return "k";

     if(a == "i" && b== '1') return "i";
     if(a == "i" && b== 'i') return "-1";
     if(a == "i" && b== 'j') return "k";
     if(a == "i" && b== 'k') return "-j";

     if(a == "j" && b== '1') return "j";
     if(a == "j" && b== 'i') return "-k";
     if(a == "j" && b== 'j') return "-1";
     if(a == "j" && b== 'k') return "i";

     if(a == "k" && b== '1') return "k";
     if(a == "k" && b== 'i') return "j";
     if(a == "k" && b== 'j') return "-i";
     if(a == "k" && b== 'k') return "-1";

     if(a == "-1" && b=='1') return "-1";
     if(a == "-1" && b=='i') return "-i";
     if(a == "-1" && b=='j') return "-j";
     if(a == "-1" && b=='k') return "-k";

     if(a == "-i" && b== '1') return "-i";
     if(a == "-i" && b== 'i') return "1";
     if(a == "-i" && b== 'j') return "-k";
     if(a == "-i" && b== 'k') return "j";

     if(a == "-j" && b== '1') return "-j";
     if(a == "-j" && b== 'i') return "k";
     if(a == "-j" && b== 'j') return "1";
     if(a == "-j" && b== 'k') return "-i";

     if(a == "-k" && b== '1') return "-k";
     if(a == "-k" && b== 'i') return "-j";
     if(a == "-k" && b== 'j') return "i";
     if(a == "-k" && b== 'k') return "1";
 }

 int main()
 {
     ifstream cin("C-small-attempt0.in");
     ofstream cout("salidaC.txt");
     int T, L, X;
     string s, linea, si="i", sj="j", sk="k";
     cin >> T;
     bool sol;
     for(int t=1; t<=T; t++){
        for(int i=0; i<100000; i++){
            arreglo[i] = "";
        }
        sol = false;
        linea = "";
        cin >> L >> X;
        cin >> s;
        for(int i=1; i<=X; i++){
            linea = linea + s;
        }
        int a = 0;
        int d = linea.size() - 1;
        if(L*X < 3){
            sol = false;
        }
        else {
            arreglo[0].push_back(linea[0]);
            for(int i=1; i<linea.size(); i++){
                arreglo[i] = f(arreglo[i-1], linea[i]);
            }
           /* for(int i=0; i<linea.size(); i++){ ///imprime
                cout << arreglo[i] << " ";
            } */
            for(int i=0; i<linea.size()-2; i++){
                if(arreglo[i] == "i"){
                    for(int j=i+1; j<linea.size()-1; j++){
                        if(arreglo[j] == "k"){
                            if(arreglo[L*X - 1] == "-1"){
                                sol = true;
                            }
                        }
                    }
                }
            }
        }
        if(sol){
            cout << "Case #" << t << ": " << "YES" << "\n";
        }
        else {
            cout << "Case #" << t << ": " << "NO" << "\n";
        }
     }
     return 0;
 }
