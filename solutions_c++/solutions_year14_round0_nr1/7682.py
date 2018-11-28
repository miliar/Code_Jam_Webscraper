// MagicTrick.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"

#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <string>
#include <fstream>


struct Question;
typedef std::array<int, 4> Row;
typedef std::array<Row, 4> Arrangement;
typedef std::array<Question, 2> Game;

struct Question
{
  Arrangement cards;
  int answer;
};

void ReadQuestion(std::istream& input, Question& question)
{
  input >> question.answer;
  Row currentRow;
  for (int row = 0; row < 4; row++)
  {      
    for (int column = 0; column < 4; column++)
    {
      input >> currentRow[column];
    }
    question.cards[row] = currentRow;
  }
}

Game ReadGame(std::istream& input)
{
  Game game;
  for (int id = 0; id < 2; id++)
  {
    ReadQuestion(input, game[id]);
  }
  return game;
}

std::vector<Game> ReadGames(std::istream& input)
{
  int totalGames = 0;
  input >> totalGames;

  std::vector<Game> games;
  for (int gameId = 0; gameId < totalGames; ++gameId)
  {
    auto game = ReadGame(input);
    games.push_back(game);
  }
  return games;
}

std::vector<Game> ReadInput(std::string filename)
{
  std::fstream input(filename, std::ios_base::in);
  
  std::vector<Game> games = ReadGames(input);
  return games;
}


void CheckResult(std::ostream& output, std::vector<int> intersection)
{
  int size = intersection.size();
  if (size == 0)
  {
    output << "Volunteer cheated!" << std::endl;
  }
  else if (size == 1)
  {
    output << intersection[0] << std::endl;
  }
  else
  {
    output << "Bad magician!" << std::endl;
  }
}

void RunGames(std::vector<Game> games)
{
  // Didn't realise I needed to send an output file, should read things really
  std::fstream output("C:\\CodingJam\\Qualification\\MagicTrick\\Output\\A-small-attempt1.out", std::ios_base::out);
  int gameNumber = 1;
  for (Game& game : games)
  {
    output << "Case #" << gameNumber++ << ": ";

    Question question = game[0];
    Row rowOne = question.cards[question.answer - 1];

    question = game[1];
    Row rowTwo = question.cards[question.answer - 1];
    
    std::sort(begin(rowOne), end(rowOne));
    std::sort(begin(rowTwo), end(rowTwo));

    std::vector<int> intersection;
    std::set_intersection(begin(rowOne), end(rowOne), 
                          begin(rowTwo), end(rowTwo), 
                          std::back_inserter(intersection));

    CheckResult(output, intersection);
  }
}

int main()
{
  auto games = ReadInput("C:\\CodingJam\\Qualification\\MagicTrick\\Input\\A-small-attempt1.in");

  RunGames(games);

	return 0;
}

