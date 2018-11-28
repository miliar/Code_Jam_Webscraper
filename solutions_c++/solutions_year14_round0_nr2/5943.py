// GJam_2014_2.cpp : définit le point d'entrée pour l'application console.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>      // std::setprecision
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	// read the input
	std::fstream myfile("input.txt", std::ios_base::in);

	fstream answer_file;
	answer_file.open( "answer.txt", std::ios_base::out );

    int nb_input;
    myfile >> nb_input;

	for( int input = 0; input < nb_input; input++ )
	{
		double C,F,X; // price, rate increase, goal
		myfile >> C >> F >> X;
		double current_rate = 2.0; // cookies per second
		int current_cookies = 0; // how many cookies now, we want X
		double current_time = 0.0;

		bool shouldBuy = true;
		while( shouldBuy )
		{
			shouldBuy = false;

			// solve the problem.
			double how_long = (X-current_cookies) / current_rate; // how long will it take two get X cookies if we don't buy a farm
		
			// when can we buy a farm ?
			double when_can_buy = 0; // right now if we have enough cookies, else
			if( current_cookies < C )
			{
				when_can_buy = (C-current_cookies) / current_rate;
			}

			if( how_long <= when_can_buy )
			{
				// don't buy !
				shouldBuy = false;
			}
			else
			{
				// if we buy a farm, is it advantageous ?
				
				// by time "how_long", will we have more cookies than if we didn't buy it ?
				double p_current_rate = current_rate + F;
				double p_current_cookies = p_current_rate * (how_long - when_can_buy );

				if( p_current_cookies > X )
				{
					// buy !
					shouldBuy = true;
				}
				else
				{
					// don't buy
					shouldBuy = false;
				}
			}

			if( shouldBuy )
			{
				// buy a factory and advances in time :
				current_time    += when_can_buy;
				current_cookies += current_rate * when_can_buy - C;
				current_rate    += F;
			}
			else
			{
				// we already computed the time :
				double answer = current_time + how_long;
				cout<<answer<<endl;
				shouldBuy = false;

				answer_file << "Case #" << input + 1<<": ";
				answer_file << std::setprecision(10) << answer << "\n";
			}
		}

	}

	system("pause");
	return 0;
}

