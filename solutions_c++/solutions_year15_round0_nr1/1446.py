//////////////////////////////////////////////////////////////////////////
// (C) 2013 Darabos, Edvárd Konrád <nil@hippy.csoma.elte.hu>
//////////////////////////////////////////////////////////////////////////
/// \file utils/cpp11.h
// Created by nil on 2013.04.13. 15:20:10
//
// Last commit:
// $Author:: nil                                                          $
// $Rev:: 1397                                                            $
// $Date:: 2014-05-15 20:41:10 +0200 (Thu, 15 May 2014)                   $
//

#pragma once

/**
 *  MS Visual Studio already supports it. Others will once.
 *  http://en.cppreference.com/w/cpp/language/override
 */
#ifndef _MSC_VER
#define override
#endif

#ifndef _MSC_VER
#define nullptr 0
#endif
