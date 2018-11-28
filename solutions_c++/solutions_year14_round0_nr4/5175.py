#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>



using namespace std;

typedef int type;
typedef double dtype;

type T,numberOfBlocks = 0;


int main(void)
{
    ifstream fin ;
    ofstream fout;
      fout.open("D-large.txt");
      fin.open("D-large.in");

    list<dtype> naomi_list;
    list<dtype> naomi_list2;
    list<dtype> ken_list;
    list<dtype> ken_list2;


    fin >> T;
    for ( type i = 0; i < T ; i++ )
     {
         naomi_list.clear();
         ken_list.clear();

         fin  >> numberOfBlocks;
         dtype naomi,ken;

         //get values to naomi
           for ( int l = 0; l < numberOfBlocks ; l++ )
                {
                    fin >> naomi;
                    naomi_list.push_front(naomi);
                }

                //get values to ken
             for ( int l = 0; l < numberOfBlocks ; l++ ){
                fin >> ken;
                ken_list.push_front(ken);
             }



           //sort the bithcas
           naomi_list.sort();
           naomi_list2.assign( naomi_list.begin() , naomi_list.end() );
           ken_list.sort();
           ken_list2.assign( ken_list.begin() , ken_list.end() );
//
//            for( list<dtype>::iterator itKen = ken_list.begin() ; itKen != ken_list.end() ; itKen++ ){
//
//                        fout << *itKen << " ";
//
//                }
//                fout << endl;

           //now is the fun
           int noCheatCount = 0;

           for( list<dtype>::iterator itNaomi = naomi_list.begin() ; itNaomi != naomi_list.end() ; itNaomi++ ){
                   // fout << *itNaomi << " ";
                for( list<dtype>::iterator itKen = ken_list.begin() ; itKen != ken_list.end() ; itKen++  ){
                        //fout << *itKen << " ";
                        if( *itKen > *itNaomi){
                            naomi_list.erase( itNaomi-- );
                            ken_list.erase( itKen-- );
                            if( itNaomi != naomi_list.begin() )
                            break;
                        }
               // fout << endl;

                }

        }


        for( list<dtype>::iterator itNaomi = ken_list2.begin() ; itNaomi != ken_list2.end() ; itNaomi++ ){
                   // fout << *itNaomi << " ";
        for( list<dtype>::iterator itKen = naomi_list2.begin() ; itKen != naomi_list2.end() ; itKen++  ){
                        //fout << *itKen << " ";
                        if( *itKen > *itNaomi){
                            naomi_list.erase( itNaomi-- );
                            ken_list.erase( itKen-- );
                            if( itNaomi != ken_list2.begin() )
                            break;
                        }
               // fout << endl;

                }

        }
     fout<< "Case #" << i+1 << ": " << numberOfBlocks-ken_list2.size() << " " <<ken_list.size() << endl;


   //  }// fout << "Case #" << i+1 << ":" << endl << "Impossible" << endl;
}
return 0;

}
