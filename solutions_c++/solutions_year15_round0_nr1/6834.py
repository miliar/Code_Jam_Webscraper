#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main(void){
   ifstream ulaz;
   ofstream izlaz;
   ulaz.open("A-large.in");
   izlaz.open("outputL.out");
   int t;
   ulaz >> t;
   for(int sluc=1;sluc<=t;++sluc){
      int maks;
      string ljudi;
      ulaz >> maks;
      ulaz >> ljudi;
      int pljescu=ljudi[0]-'0';
      int fali=0;
      for(int i=1;i<=maks;++i){
         if(i<=pljescu)
            pljescu+=(ljudi[i]-'0');
         else{
            fali+=(i-pljescu);
            pljescu+=(i-pljescu);
            pljescu+=(ljudi[i]-'0');
         }
      }
      izlaz << "Case #" << sluc <<": " << fali << endl;
   }

   ulaz.close();
   izlaz.close();
   return 0;
}
