#ifndef _KL_PRECOMPILATION_HPP_
#define _KL_PRECOMPILATION_HPP_

// Include file for std::cout, std::cin
#include<iostream>

#include<stdio.h>


// For clock time and time duration stats
#include <time.h>

#include <map>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <utility>
#include <list>
#include <queue>
#include <stack>

using namespace std;

namespace kewl_Library
{
	// For loop
#define FOR(i, first, last, increment) for (int i = (first); i < (last); i = i + (increment))
#define KL_FOR FOR



	// Default For loop with variable name "i", first = 0, increment = 1
#define FOR_DEF(i, last) KL_FOR(i, 0, last, 1)
#define KL_FOR_DEF FOR_DEF


	// Dont care about the looping variable name
	// TODO : Need to solve the problem of generating a unique temp loop var, for now __i__ suffices
#define REPEAT(N) for (int __i__ = 0; __i__ < (N); ++__i__)



	// Reverse For loop
#define R_FOR(i, first, last, increment) for (int i = ((first) - 1); i >= (last); i = i - (increment))
#define KL_R_FOR R_FOR



	// Default For loop with variable name "i", first = 0, increment = 1
#define R_FOR_DEF(i, first) KL_R_FOR(i, first, 0, 1)
#define KL_R_FOR_DEF R_FOR_DEF

	typedef unsigned long long int ulli_t;
	typedef vector<ulli_t> uivector_t;
	typedef uivector_t::iterator uivector_it_t;
	typedef uivector_t::const_iterator uivector_cit_t;


	typedef long long int lli_t;
	typedef lli_t LLI;
	typedef vector<lli_t> ivector_t;
	typedef ivector_t::iterator ivector_it_t;
	typedef ivector_t::const_iterator ivector_cit_t;



	typedef long double LD_t;


/*	-------	BEWARE -	macros can't be overloaded i.e. both the 'read's below	
						can't have the same name	---------- */
#define read1(n) cin >> n;
#define read2(m, n) cin >> m >> n;
#define read3(m, n, o) cin >> m >> n >> 0;
// #define readArr(n, size) KL_FOR_DEF(i, size) { cin >> n[i]; } 
#define readArr1D(n, size)	KL_FOR_DEF(i, size)	\
							{					\
								cin >> n[i];	\
							} 

#define write1(n) cout << n;
#define write2(m, n) cout << m << n;
#define write3(m, n, o) cout << m << n << o;
#define writeArr1D(n, size)	KL_FOR_DEF(i, size)	\
							{					\
								cout << n[i];	\
							} 

#define DBG(x)              cout<<__LINE__<<" :: "<<#x<< ": "<<x<<endl;
#define DBG2(x, y)          cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<endl;
#define DBG3(x, y, z)       cout<<__LINE__<<" :: "<<#x<< ": "<<x<<" | "<<#y<< ": "<<y<<" | "<<#z<<": "<<z<<endl;
#define DBG4(a, b, c, d)    cout<<__LINE__<<" :: "<<#a<< ": "<<a<<" | "<<#b<< ": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;

};
#endif  // _KL_PRECOMPILATION_HPP_
