#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <iomanip>

#include <string>
#include <cstring>

#include <vector>

#include <algorithm>
#include <limits.h>
#include <math.h>
#include <cfloat>

#include <assert.h>
#include <unistd.h>

#define CODE_DEBUG 1
#if CODE_DEBUG
#define LOGD(str) do { std::cout << "+++++ " << str << std::endl; } while( false )
#define LOGD_INL(str) do{ std::cout << str; } while( false )
#else
#define LOGD(str) do { } while ( false )
#define LOGD_INL(str) do { } while ( false )
#endif

using namespace std;

bool weight_cmp_asc(const double &lhs, const double &rhs) {
    return (lhs<rhs);
}
bool weight_cmp_desc(const double &lhs, const double &rhs) {
    return (lhs>rhs);
}

void shift_mass_to_back(vector<double>& arr, int p) {
    double val=0;

    vector<double>::iterator iter;
    iter = arr.begin()+p;

    val = *iter;
    arr.erase(iter);
    arr.push_back(val);
}


int main()
{
    int tcases;
    int n, y, z;

    vector<double> naomi;
    vector<double> naomi_prev;
    vector<double> ken;
    vector<double> ken_prev;

    vector<double>::iterator iter;

    double mass;
    double ken_heavist;

    cin >> tcases;
    cin.ignore();
    for(int t=1; t<=tcases; t++) {
        cin >> n;
        cin.ignore();

        for(int i=0; i<n; i++) {
            cin >> mass;
            naomi_prev.push_back(mass);
        }
        cin.ignore();
        for(int i=0; i<n; i++) {
            cin >> mass;
            ken_prev.push_back(mass);
        }


        // move naomi's mass...to maximize
        y = 0;
        sort( ken_prev.begin(), ken_prev.end(), weight_cmp_desc );
        for(int i=0; i<n; i++) {
            sort( naomi_prev.begin(), naomi_prev.end(), weight_cmp_asc );
            if( ken_prev[i]>naomi_prev.back() ) {
                iter = naomi_prev.begin();
                naomi.push_back(*iter);
                naomi_prev.erase(iter);
            } else {
                while( ken_prev[i]>naomi_prev.front() ) {
                    shift_mass_to_back(naomi_prev,0);
/*                    
                    cout << "[debug_#1] ken_p = ";
                    for(int r=0; r<ken_prev.size(); r++) {
                        cout << "\t" << ken_prev[r];
                    }
                    cout << endl;
                    cout << "[debug_#1] naomi_p = ";
                    for(int r=0; r<naomi_prev.size(); r++) {
                        cout << "\t" << naomi_prev[r];
                    }
                    cout << endl;
                    cout << "[debug_#1] naomi = ";
                    for(int r=0; r<naomi.size(); r++) {
                        cout << "\t" << naomi[r];
                    }
                    cout << endl << endl;
*/                    
                }
                iter = naomi_prev.begin();
                naomi.push_back(*iter);
                naomi_prev.erase(iter);
                y++;
            }
        }

        // move ken's mass...to maximize
        z = 0;
        sort( naomi.begin(), naomi.end(), weight_cmp_desc );
        for(int i=0; i<n; i++) {
            sort( ken_prev.begin(), ken_prev.end(), weight_cmp_asc );
            if( naomi[i]>ken_prev.back() ) {
                iter = ken_prev.begin();
                ken.push_back(*iter);
                ken_prev.erase(iter);
                z++;
            } else {
                while( naomi[i]>ken_prev.front() ) {
                    shift_mass_to_back(ken_prev,0);
/*                    
                    cout << "[debug_#2] naomi = ";
                    for(int r=0; r<naomi.size(); r++) {
                        cout << "\t" << naomi[r];
                    }
                    cout << endl;
                    cout << "[debug_#2] ken_p = ";
                    for(int r=0; r<ken_prev.size(); r++) {
                        cout << "\t" << ken_prev[r];
                    }
                    cout << endl;
                    cout << "[debug_#2] ken = ";
                    for(int r=0; r<ken.size(); r++) {
                        cout << "\t" << ken[r];
                    }
                    cout << endl << endl;
*/                    
                }
                iter = ken_prev.begin();
                ken.push_back(*iter);
                ken_prev.erase(iter);
            }
        }
/*
        z = 0;
        sort( ken.begin(), ken.end(), weight_cmp_asc );
        for(int i=0; i<n; i++) {
            if( naomi[i]>ken[i] ) {
                if( naomi[i]>*max_element(ken.begin()+i,ken.end()) ) {
                    z = n-i;
                    break;
                } else {
                    while( naomi[i]>ken[i] ) {
                        shift_mass_to_back(ken,i);
                        cout << "[debug] naomi = ";
                        for(int r=0; r<n; r++) {
                            cout << " " << naomi[r];
                        }
                        cout << endl;
                        cout << "[debug] ken = ";
                        for(int r=0; r<n; r++) {
                            cout << " " << ken[r];
                        }
                        cout << endl << endl;
                    }
                }
            }
        }
*/
        cout << "Case #" << t << ": " << y << " " << z << endl;

        naomi_prev.clear();
        naomi.clear();
        ken.clear();
    }
}

