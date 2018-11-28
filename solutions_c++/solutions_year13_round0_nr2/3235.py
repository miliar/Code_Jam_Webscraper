
//----------------------------------------------------------------------------
// Require-header-file(s)
//----------------------------------------------------------------------------

// Standard-library
#include <iostream>
#include <fstream>

//----------------------------------------------------------------------------
// Common using types
//----------------------------------------------------------------------------

typedef size_t                           size_type;
typedef char                             char_type;
typedef std::basic_ifstream< char_type > ifst_type;
typedef std::basic_ofstream< char_type > ofst_type;

enum { BUFF_SIZE = 101 };
typedef size_type buff_type[BUFF_SIZE][BUFF_SIZE];

//----------------------------------------------------------------------------
//! \brief Load the input data from the target input file stream.
//! \param ifst Target input file stream.
//! \param buff Buffer that will held the loaded input.
//! \param rows Number of rows.
//! \param cols Number of columns.
//! \return Either
//!   \li true, if loading success.
//!   \li false, otherwise.
//----------------------------------------------------------------------------

bool load_buff( ifst_type & ifst, 
                buff_type & buff,
                size_type & rows,
                size_type & cols )
{
  if( false == !!(ifst >> rows >> cols) )
    return false;

  for( size_type i = 0; i < rows; ++i )
  for( size_type j = 0; j < cols; ++j )
  {
    if( false == !!(ifst >> buff[i][j]) )
      return false;
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Evaluate the game result.
//! \param buff Buffer that held the current game state.
//! \param rows Number of rows.
//! \param cols Number of columns.
//! \return Either
//!   \li true, if evaluation success.
//!   \li false, otherwise.
//----------------------------------------------------------------------------

bool eval_buff( buff_type & buff,
                size_type   rows,
                size_type   cols )
{
  // Get the max value of each row
  for( size_type i = 0; i < rows; ++i )
  {
    size_type & rmax = buff[i][cols];
    for( size_type j = 0; j < cols; ++j )
      rmax = std::max( rmax, buff[i][j] );
  }

  // Get the max value of each row
  for( size_type j = 0; j < cols; ++j )
  {
    size_type & cmax = buff[rows][j];
    for( size_type i = 0; i < rows; ++i )
      cmax = std::max( cmax, buff[i][j] );
  }

  // Check if it is possible or not
  for( size_type i = 0; i < rows; ++i )
  {
    size_type rmax = buff[i][cols];
    for( size_type j = 0; j < cols; ++j )
    {
      size_type cmax = buff[rows][j];
      size_type curr = buff[i][j];
      if( (rmax > curr) && (cmax > curr) )
        return false;
    }
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Main entrance of this program.
//! \param argc, number of input arguments.
//! \param argv, list of input arguments.
//! \return 0 if program exits successfully.
//----------------------------------------------------------------------------

int main( int     argc, 
          char ** argv )
{
  char const * file_i = argv[1];
  char const * file_o = argv[2];
  if( argc != 3 )
  {
    std::wcerr << "Usage: ./run.out <input-file> <output-file>" << std::endl;
    return 1;
  }

  ifst_type ifst( file_i );
  if( false == ifst.is_open( ) )
  {
    std::wcerr << "Error: Unable to open file '" << file_i << "'." << std::endl;
    return 1;
  }

  ofst_type ofst( file_o );
  if( false == ofst.is_open( ) )
  {
    std::wcerr << "Error: Unable to create file '" << file_o << "'." << std::endl;
    return 1;
  }

  size_type loop = 0;
  if( false == !!(ifst >> loop) )
  {
    std::wcerr << "Error: Found invalid number of loops." << std::endl;
    return 1;
  }

  for( size_type i = 0; i < loop; ++i )
  {
    buff_type buff = { 0 };
    size_type rows = 0;
    size_type cols = 0;

    if( false == load_buff( ifst, buff, rows, cols ) )
    {
      std::wcerr << "Error: Unable to load input data #" << i << "." << std::endl;
      return 1;
    }

    if( false == eval_buff( buff, rows, cols ) )
    {
      ofst << "Case #" << (i+1) << ": NO" << std::endl;
    }
    else
    {
      ofst << "Case #" << (i+1) << ": YES" << std::endl;
    }
  }

  return 0;
}

//----------------------------------------------------------------------------
// End-of-file
//----------------------------------------------------------------------------

