#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define DEBUG
#undef DEBUG

int main(int argc, char *argv[]) 
{
    int i, j, k;
    int case_no = 0;
    int num_blk=0;
    int score_at_deceitful_war, score_at_war;
    double tmp;
    ifstream fp;
    vector<double> naomi;
    vector<double> ken;

    fp.open(argv[1]);
    if(!fp.is_open()) { cout<<"File open error!"<<endl; }
    
    fp>>case_no;
    for( i = 0 ; i < case_no ; i++ ) {
        
        //parsing 
        fp>>num_blk;
        //initialing
        score_at_deceitful_war = 0;
        score_at_war = num_blk;

        naomi.clear();
        ken.clear();

        for( j = 0 ; j < num_blk ; j++ ) { 
            fp>>tmp;
            naomi.push_back(tmp);
        }
        for( j = 0 ; j < num_blk ; j++ ) { 
            fp>>tmp;
            ken.push_back(tmp);
        }

        
        //*************************************//
        //Algorithm
        //*************************************//
        sort( naomi.begin(), naomi.end() );
        sort( ken.begin(), ken.end());
#ifdef DEBUG
        cout<<"naomi: ";
        for( j = 0 ; j < num_blk ; j++ ) { 
            cout<<naomi[j]<<" ";
        }
        cout<<endl;
        cout<<"ken: ";
        for( j = 0 ; j < num_blk ; j++ ) { 
            cout<<ken[j]<<" ";
        }
        cout<<endl;
#endif

        // optmial decetiful_war score every number larger than ken's
        // smallest naomi's block will never win
        int max_idx = 0;
        for( j = 0 ; j < num_blk && max_idx < num_blk ; j++ ) { 
                if( naomi[j] > ken[max_idx] ) {
                    score_at_deceitful_war++;
                    max_idx++;
                }
        }
        // largest ken's block will be unbeatable 
        /*
        for( j = num_blk-1 ; j >=0 ; j-- ) { 
            if( naomi[num_blk-1] < ken[j] ) {
                score_at_deceitful_war--;
            } else {
                break;
            }
        }
        */
        //if ( score_at_deceitful_war < 0 ) {
        //        score_at_deceitful_war = 0;
        //}
        // optmial war score?
        for( j = num_blk-1 ; j >=0 ; j-- ) { 
            int get_one = 0;
            for( k = 0 ; k < ken.size() ; k++ ) {
                if( naomi[j] < ken[k] ) {
                    score_at_war--;
                    ken.erase( ken.begin() + k );
                    get_one = 1;
                    break;
                }
            }
            if(!get_one) {
                ken.erase(ken.begin());
            }
        }


        //*************************************//
        
        // Report Message
		cout<<"Case #"<<i+1<<": "<<score_at_deceitful_war<<" "<<score_at_war<<endl;
    }
    
    fp.close();
    return 0;

}
